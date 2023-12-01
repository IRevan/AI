import os
import pandas as pd
import olefile
import zlib
import struct

path = "./data/"
file_list = os.listdir(path)
file_list_hwp = [file for file in file_list if file.endswith(".hwp")]
file_list_hwp.sort()

sr_hwp = pd.Series(file_list_hwp)

class HWPExtractor(object):
    FILE_HEADER_SECTION = "FileHeader"
    HWP_SUMMARY_SECTION = "\x05HwpSummaryInformation"
    SECTION_NAME_LENGTH = len("Section")
    BODYTEXT_SECTION = "BodyText"
    HWP_TEXT_TAGS = [67]

    def __init__(self, filename):
        self._ole = self.load(filename)
        self._dirs = self._ole.listdir()

        self._valid = self.is_valid(self._dirs)
        if (self._valid == False):
            raise Exception("Not Valid HwpFile")

        self._compressed = self.is_compressed(self._ole)
        self.text = self._get_text()

    # 파일 불러오기
    def load(self, filename):
        return olefile.OleFileIO(filename)

    # hwp 파일인지 확인 header가 없으면 hwp가 아닌 것으로 판단하여 진행 안함
    def is_valid(self, dirs):
        if [self.FILE_HEADER_SECTION] not in dirs:
            return False

        return [self.HWP_SUMMARY_SECTION] in dirs

    # 문서 포맷 압축 여부를 확인
    def is_compressed(self, ole):
        header = self._ole.openstream("FileHeader")
        header_data = header.read()
        return (header_data[36] & 1) == 1

    # bodytext의 section들 목록을 저장
    def get_body_sections(self, dirs):
        m = []
        for d in dirs:
            if d[0] == self.BODYTEXT_SECTION:
                m.append(int(d[1][self.SECTION_NAME_LENGTH:]))

        return ["BodyText/Section" + str(x) for x in sorted(m)]

    # text를 뽑아내는 함수
    def get_text(self):
        return self.text

    # 전체 text 추출
    def _get_text(self):
        sections = self.get_body_sections(self._dirs)
        text = ""
        for section in sections:
            text += self.get_text_from_section(section)
            text += "\n"

        self.text = text
        return self.text

    # section 내 text 추출
    def get_text_from_section(self, section):
        bodytext = self._ole.openstream(section)
        data = bodytext.read()

        unpacked_data = zlib.decompress(data, -15) if self.is_compressed else data
        size = len(unpacked_data)

        i = 0

        text = ""
        while i < size:
            header = struct.unpack_from("<I", unpacked_data, i)[0]
            rec_type = header & 0x3ff
            level = (header >> 10) & 0x3ff
            rec_len = (header >> 20) & 0xfff

            if rec_type in self.HWP_TEXT_TAGS:
                rec_data = unpacked_data[i + 4:i + 4 + rec_len]
                text += rec_data.decode('utf-16')
                text += "\n"

            i += 4 + rec_len

        return text


# text 추출 함수 -> 이 함수를 사용하면 됨
def get_text(filename):
    hwp = HWPExtractor(filename)
    return hwp.get_text()

f = get_text(path + sr_hwp[0])
print(f)

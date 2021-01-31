import win32clipboard
import re


class ClipboardManager(object):
    @staticmethod
    def set_clipboard(data):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        encoded_data = data.encode('utf-8')
        format = win32clipboard.RegisterClipboardFormat('XML SpreadSheet')
        win32clipboard.SetClipboardData(format, encoded_data)
        win32clipboard.CloseClipboard()

    @staticmethod
    def format_string(s):
        tmp = s.split('<em class="green_text">')
        tokens = []
        for token in tmp:
            if token.find('</em>') > -1:
                f, e = token.split('</em>')
                tokens.extend([(1, f), (0, e)])
            else:
                tokens.append((0, token))

        data = ''
        for token in tokens:
            if token[0] == 0:
                data += f'<Font>{token[1]}</Font>'
            else:
                data += f'<U><Font html:Color="#305496">{token[1]}</Font></U>'

        template = '''<?xml version="1.0"?>
<?mso-application progid="Excel.Sheet"?>
<Workbook xmlns="urn:schemas-microsoft-com:office:spreadsheet"
 xmlns:o="urn:schemas-microsoft-com:office:office"
 xmlns:x="urn:schemas-microsoft-com:office:excel"
 xmlns:ss="urn:schemas-microsoft-com:office:spreadsheet"
 xmlns:html="http://www.w3.org/TR/REC-html40">
 <Styles>
  <Style ss:ID="Default" ss:Name="Normal">
   <Alignment ss:Vertical="Center"/>
   <Borders/>
   <Font ss:FontName="맑은 고딕" x:CharSet="129" x:Family="Modern" ss:Size="11"
    ss:Color="#000000"/>
   <Interior/>
   <NumberFormat/>
   <Protection/>
  </Style>
  <Style ss:ID="s66">
   <Alignment ss:Vertical="Center"/>
   <Borders/>
   <Font ss:FontName="맑은 고딕" x:CharSet="129" x:Family="Modern" ss:Size="11"
    ss:Color="#FF00FF" ss:Underline="Single"/>
   <Interior/>
   <NumberFormat/>
   <Protection/>
  </Style>
 </Styles>
 <Worksheet ss:Name="Sheet1">
  <Table ss:ExpandedColumnCount="1" ss:ExpandedRowCount="1"
   ss:DefaultColumnWidth="54" ss:DefaultRowHeight="16.5">
   <Row>
    <Cell ss:StyleID="s66"><ss:Data ss:Type="String"
      xmlns="http://www.w3.org/TR/REC-html40">''' + data + '''</ss:Data></Cell>
   </Row>
  </Table>
 </Worksheet>
</Workbook>'''
        return template + '\x00'


if __name__ == '__main__':
    ClipboardManager.set_clipboard(ClipboardManager.format_string('<em class="green_text">본 지침은</em> <em class="green_text">모든 회사의</em> 정보자산에 대하여 적용한다.'))

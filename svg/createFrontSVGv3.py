# Open a file with access mode 'w' (not 'a' - we want to overwrite)
# Change the default filename in next line UHR114......svg
file_object = open('UHR114_Front_CH_Segoe UI Bold.svg', 'w', encoding='utf-8')

startX = 239.5
startY = 1129
spacing_x = 63
spacing_y = 69.9213
textSize = 40
fontFamily = "Segoe UI Bold"  # choose your font. Any you have installed. 

# The text organized by rows
text_rows = [
    "ÄSBISCHUFÜF",
    "VIERTUNFZÄÄ",
    "ZWÄNZGSEVOR",
    "ABCHAUBIECM",
    "EISZWEISDRÜ",
    "VIERIFÜFIST",
    "SÄCHSISIBNI",
    "ACHTINÜNIEL",
    "ZÄNIECHEUFI",
    "ZWÖUFIENGSI"
]

file_object.write('''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   enable-background="new 0 0 1726.3 861.732"
   height="300mm"
   viewBox="0 0 1133.8582 1133.8583"
   width="300mm"
   version="1.1"
   id="svg918"
   inkscape:version="0.92.4 (5da689c313, 2019-01-14)">
  <metadata
     id="metadata924">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title></dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <defs
     id="defs922" />
  <sodipodi:namedview
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1"
     objecttolerance="10"
     gridtolerance="10"
     guidetolerance="10"
     inkscape:pageopacity="0"
     inkscape:pageshadow="2"
     inkscape:window-width="1920"
     inkscape:window-height="1109"
     id="namedview920"
     showgrid="false"
     inkscape:zoom="0.31115"
     inkscape:cx="-90.764306"
     inkscape:cy="1012.9005"
     inkscape:window-x="1920"
     inkscape:window-y="0"
     inkscape:window-maximized="1"
     inkscape:current-layer="g916"
     inkscape:document-units="mm" />
  <g
     transform="translate(0,-861.73197)"
     id="g916">
    <path
       d="M 0,861.73194 H 1133.8582 V 1995.5902 H 0 Z"
       id="path2"
       inkscape:connector-curvature="0"
       style="fill:#000055;fill-opacity:0.16470588;stroke-width:1.33317006" />
    <path
       d="m 953.27735,1806.6423 c 0,4.6954 -3.80621,8.5043 -8.50297,8.5043 -4.69544,0 -8.50298,-3.8076 -8.50298,-8.5043 0,-4.6968 3.80754,-8.5043 8.50298,-8.5043 4.69676,10e-4 8.50297,3.8088 8.50297,8.5043"
       id="path4"
       inkscape:connector-curvature="0"
       style="stroke-width:1.33317304" />
    <circle
       cx="944.77441"
       cy="1806.6422"
       r="8.5029774"
       id="circle6" />
    <path
       d="m 197.46292,1806.6423 c 0,4.6954 -3.80621,8.5043 -8.50298,8.5043 -4.69543,0 -8.50298,-3.8076 -8.50298,-8.5043 0,-4.6968 3.80755,-8.5043 8.50298,-8.5043 4.69677,10e-4 8.50298,3.8088 8.50298,8.5043"
       id="path8"
       inkscape:connector-curvature="0"
       style="stroke-width:1.33317304" />
    <circle
       cx="188.95993"
       cy="1806.6422"
       r="8.5029774"
       id="circle10" />
    <path
       d="m 197.46292,1050.8305 c 0,4.6954 -3.80621,8.503 -8.50298,8.503 -4.69543,0 -8.50298,-3.8076 -8.50298,-8.503 0,-4.6954 3.80755,-8.503 8.50298,-8.503 4.69677,0 8.50298,3.8076 8.50298,8.503"
       id="path12"
       inkscape:connector-curvature="0"
       style="stroke-width:1.33317304" />
    <circle
       cx="188.95993"
       cy="1050.8304"
       r="8.5029774"
       id="circle14" />
    <path
       d="m 953.27735,1050.8305 c 0,4.6954 -3.80621,8.503 -8.50297,8.503 -4.69544,0 -8.50298,-3.8076 -8.50298,-8.503 0,-4.6954 3.80754,-8.503 8.50298,-8.503 4.69676,0 8.50297,3.8076 8.50297,8.503"
       id="path16"
       inkscape:connector-curvature="0"
       style="stroke-width:1.33317304" />
    <circle
       cx="944.77441"
       cy="1050.8304"
       r="8.5029774"
       id="circle18" />''')

textId = 65
tspanId = 67

for row_num, row_text in enumerate(text_rows):
    for col_num, char in enumerate(row_text):
        variable_x_spacing = str(startX + col_num * spacing_x - (2.1 if col_num != 0 else 0))
        file_object.write(f'''    <text
       xml:space="preserve"
       style="font-style:normal;font-weight:normal;font-size:{textSize}px;line-height:1.25;font-family:{fontFamily};letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none"
       x="{variable_x_spacing}"
       y="{startY + row_num * spacing_y}"
       id="text{textId + col_num * 2}"><tspan
         sodipodi:role="line"
         id="tspan{tspanId + col_num * 2}"
         x="{variable_x_spacing}"
         y="{startY + row_num * spacing_y}">{char}</tspan></text>
''')

file_object.write("""</g>\n</svg>""")
file_object.close()
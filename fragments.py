header = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
   "http://www.w3.org/TR/html4/strict.dtd">
<html>
  <head>
    <link href="style.css" rel="stylesheet" type="text/css">
    </style>
    <script src="drive.js">
    </script>
  </head>
  <body>
    <div id="outer">"""
footer = """
    </div>
  </body>
</html>
"""
def wrap(text):
    return "\n".join((header, text, footer))

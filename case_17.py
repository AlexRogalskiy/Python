#!/usr/bin/python
 
from gimpfu import *
 
def first_plugin(timg, tdrawable):
  print "Hello, world!"
 
register(
  "hello_world",
  "Presents a Hello, World! message",
  "Presents a Hello, World! message",
  "Brad Jones",
  "Brad Jones",
  "2017",
  "<Image>/Image/Hello, World!",
  "RGB*, GRAY*",
  [],
  [],
  first_plugin)
 
main()

#!/usr/bin/env python

from gimpfu import *

def test_script(customtext, font, size):
  img = gimp.Image(1, 1, RGB)
  layer = pdb.gimp_text_fontname(img, None, 0, 0, customtext, 10, True, size, PIXELS, font)
  img.resize(layer.width, layer.height, 0, 0)
  gimp.Display(img)
  gimp.displays_flush()

register(
 "python_test",
 "TEST",
 "TEST",
 "Brad Jones",
 "Brad Jones",
 "2017",
 "TEST",
 "",
 [
 (PF_STRING, "customtext", "Text string", 'Scripting is handy!'),
 (PF_FONT, "font", "Font", "Sans"),
 (PF_SPINNER, "size", "Font size", 100, (1, 3000, 1)),
 ],
 [],
 test_script, menu="<Image>/File/Create")

main()

#!/usr/bin/env python

from gimpfu import *

def invert_current_layer(img, layer):
  pdb.gimp_invert(layer)
 
register(
  "python_fu_invert_current_layer",
  "Invert layer",
  "Invert colors in the current layer",
  "Brad Jones",
  "Brad Jones",
  "2017",
  "<Image>/Filters/Custom/Invert current layer",
  "*",
  [],
  [],
  invert_current_layer)
 
main()
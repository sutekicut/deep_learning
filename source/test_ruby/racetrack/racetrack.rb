#====================
# racetrack.rb
#====================

module Racetrack

  # 以下の文字列でコースを表現する
  START = 'S'
  IN = '.'
  OUT = 'o'
  GOAL = 'G'

  # 最高スピードの絶対値
  MAX_SPEED = 4

end

# コース1
COURSE1 = <<__END_OF_COURSE1__
ooooooooooooooooooooooooo
ooooooooooooooooooooooooo
ooooooooooooooooooooooooo
ooooooooooooooooooooooooo
ooooooo.............Goooo
oooooo..............Goooo
oooooo..............Goooo
ooooo...............Goooo
oooo................Goooo
oooo................Goooo
oooo..........ooooooooooo
oooo.........oooooooooooo
oooo.........oooooooooooo
oooo.........oooooooooooo
oooo.........oooooooooooo
oooo.........oooooooooooo
oooo.........oooooooooooo
oooo.........oooooooooooo
ooooo........oooooooooooo
ooooo........oooooooooooo
ooooo........oooooooooooo
ooooo........oooooooooooo
ooooo........oooooooooooo
ooooo........oooooooooooo
ooooo........oooooooooooo
ooooo........oooooooooooo
oooooo.......oooooooooooo
oooooo.......oooooooooooo
oooooo.......oooooooooooo
oooooo.......oooooooooooo
oooooo.......oooooooooooo
oooooo.......oooooooooooo
oooooo.......oooooooooooo
ooooooo......oooooooooooo
ooooooo......oooooooooooo
oooooooSSSSSSoooooooooooo
ooooooooooooooooooooooooo
ooooooooooooooooooooooooo
ooooooooooooooooooooooooo
ooooooooooooooooooooooooo
__END_OF_COURSE1__

# コース2
COURSE2 = <<__END_OF_COURSE2__
oooooooooooooooooooooooooooooooooooooooo
oooooooooooooooooooooooooooooooooooooooo
oooooooooooooooooooooooooooooooooooooooo
oooooooooooooooooooooooooooooooooooooooo
oooooooooooooooooooo...............Goooo
ooooooooooooooooo..................Goooo
oooooooooooooooo...................Goooo
ooooooooooooooo....................Goooo
ooooooooooooooo....................Goooo
ooooooooooooooo....................Goooo
ooooooooooooooo....................Goooo
oooooooooooooooo...................Goooo
ooooooooooooooooo..................Goooo
oooooooooooooooooo................oooooo
oooooooooooooooooo.............ooooooooo
oooooooooooooooooo............oooooooooo
oooooooooooooooooo..........oooooooooooo
oooooooooooooooooo.........ooooooooooooo
ooooooooooooooooo..........ooooooooooooo
oooooooooooooooo...........ooooooooooooo
ooooooooooooooo............ooooooooooooo
oooooooooooooo.............ooooooooooooo
ooooooooooooo..............ooooooooooooo
oooooooooooo...............ooooooooooooo
ooooooooooo................ooooooooooooo
oooooooooo.................ooooooooooooo
ooooooooo..................ooooooooooooo
oooooooo...................ooooooooooooo
ooooooo....................ooooooooooooo
oooooo.....................ooooooooooooo
ooooo......................ooooooooooooo
oooo.......................ooooooooooooo
oooo.......................ooooooooooooo
ooooSSSSSSSSSSSSSSSSSSSSSSSooooooooooooo
oooooooooooooooooooooooooooooooooooooooo
oooooooooooooooooooooooooooooooooooooooo
oooooooooooooooooooooooooooooooooooooooo
oooooooooooooooooooooooooooooooooooooooo
__END_OF_COURSE2__
#====================
# policy.rb
#====================

require './rental_car_problem'

module RentalCarProblem
  class Policy
    # 方策の初期値は0（移動しない）
    def initialize
      @policy = Array.new((0..RENTAL_CAR_MAX).size) do
        Array.new((0..RENTAL_CAR_MAX).size, 0)
      end
    end

    def get(x, y)
      return @policy[x][y]
    end

    def set(x, y, move)
      @policy[x][y] = move
    end

    @@print_header = "   |" + " %02d" * (0..RENTAL_CAR_MAX).size
    @@print_bar = "----" + "---" * (0..RENTAL_CAR_MAX).size
    @@print_format = "%02d |" + " %2d" * (0..RENTAL_CAR_MAX).size

    def print
      puts @@print_bar
      puts sprintf @@print_header, *((0..RENTAL_CAR_MAX).to_a)
      puts @@print_bar
      (0..RENTAL_CAR_MAX).each do |i|
        puts sprintf @@print_format, i, *((0..RENTAL_CAR_MAX).map {|j| @policy[i][j]})
      end
      puts @@print_bar
    end
  end
end
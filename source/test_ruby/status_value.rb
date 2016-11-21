#====================
# status_value.rb
#====================

require './rental_car_problem'

module RentalCarProblem
  class StatusValue
    # 状態価値の初期値は0
    def initialize
      @value = Array.new((0..RENTAL_CAR_MAX).size) do
        Array.new((0..RENTAL_CAR_MAX).size, 0.0)
      end
    end

    def get(x, y)
      @value[x][y]
    end

    def set(x, y, new_value)
      @value[x][y] = new_value
    end

    @@print_header = "   |" + "    %02d" * (0..RENTAL_CAR_MAX).size
    @@print_bar = "----" + "------" * (0..RENTAL_CAR_MAX).size
    @@print_format = "%02d |" + " %5.1f" * (0..RENTAL_CAR_MAX).size

    def print
      puts @@print_bar
      puts sprintf @@print_header, *((0..RENTAL_CAR_MAX).to_a)
      puts @@print_bar
      (0..RENTAL_CAR_MAX).each do |i|
        puts sprintf @@print_format, i, *((0..RENTAL_CAR_MAX).map {|j| @value[i][j]})
      end
      puts @@print_bar
    end

    # 状態(x, y)からmoveだけ動かしたときの状態価値を計算する
    # moveが不正な場合、例外を投げる
    def value_of_move(x, y, move)
      value = 0.0

      # まず、moveだけ車を移動させる
      # これが次の日に各営業所にある車の台数
      # ただし、値が不正なら、例外を投げる
      next_x_start = x - move
      next_y_start = y + move
      if (next_x_start < 0) || (next_x_start > RENTAL_CAR_MAX) ||
         (next_y_start < 0) || (next_y_start > RENTAL_CAR_MAX)
        raise "move is invalid."
      end

      # 第1で貸し出せるのは、0〜next_x_startまで
      # 第2で貸し出せるのは、0〜next_y_startまで
      (0..next_x_start).each do |x_rental|
        (0..next_y_start).each do |y_rental|
          x_rest = next_x_start - x_rental
          y_rest = next_y_start - y_rental
          # 第1に返される台数は、0〜(RENTAL_CAR_MAX - x_rest)まで
          # 第2に返される台数は、0〜(RENTAL_CAR_MAX - y_rest)まで
          (0..(RENTAL_CAR_MAX - x_rest)).each do |x_return|
            (0..(RENTAL_CAR_MAX - y_rest)).each do |y_return|
              probability = (
                x_rental_probability(x_rental) *
                y_rental_probability(y_rental) *
                x_return_probability(x_return) *
                y_return_probability(y_return))
              reward = (x_rental + y_rental) * 10 - move.abs * 2
              next_x = next_x_start - x_rental + x_return
              next_y = next_y_start - y_rental + y_return
              value += probability * (reward + 0.9 * @value[next_x][next_y])
            end
          end
        end
      end
      puts value
      return value
    end

    def get_most_valuable_move(x, y, *move_list)
      move_value_hash = move_list.each_with_object(Hash.new) do |move, hash|
        begin
          hash[move] = value_of_move(x, y, move)
        rescue
          # 不正な移動の場合、処理をスキップ
        end
      end

      highest_value = move_value_hash.values.max
      most_valuable_move = move_value_hash.key(highest_value)

      return most_valuable_move, highest_value
    end

    private

    # 期待値がexpectでのポアソン分布の確率P(X=n)を返す
    def poisson(n, expect)
      if n > 0
        (expect ** n) * (Math.exp(-expect)) / (1..n).inject(:*)
      else
        Math.exp(-expect)
      end
    end

    # 第1営業所の貸出数がnになる確率を返す
    def x_rental_probability(n)
      poisson(n, 3)
    end

    # 第2営業所の貸出数がnになる確率を返す
    def y_rental_probability(n)
      poisson(n, 4)
    end

    # 第1営業所の返却数がnになる確率を返す
    def x_return_probability(n)
      poisson(n, 3)
    end

    # 第2営業所の返却数がnになる確率を返す
    def y_return_probability(n)
      poisson(n, 2)
    end
  end
end
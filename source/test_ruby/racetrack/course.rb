#====================
# course.rb
#====================

require './racetrack'

module Racetrack

  class Course

    # コースを表す文字列からコースを作成する
    def initialize(course)
      @course_info = Array.new
      @starts = Array.new
      course.each_line.with_index do |line, y|
        line_info = Array.new
        line.each_char.with_index do |c, x|
          line_info.push c
          if c == START
            @starts.push to_state(x, y, 0, 0)
          end
        end
        line_info.freeze
        @course_info.push line_info
      end
      @course_info.freeze
      @starts.freeze
    end

    attr_reader :starts

    def in?(state)
      to_course_info(state) == IN
    end

    def out?(state)
      to_course_info(state) == OUT
    end

    def start?(state)
      to_course_info(state) == START
    end

    def goal?(state)
      to_course_info(state) == GOAL
    end

    # 可能な行動の集合を返す
    def get_valid_actions(state)
      vx, vy = to_speed(state)

      valid_actions = Array.new
      (-1..1).each do |ax|
        (-1..1).each do |ay|
          new_vx = vx + ax
          new_vy = vy + ay
          if (new_vx.abs <= MAX_SPEED &&
              new_vy.abs <= MAX_SPEED &&
              new_vx.abs + new_vy.abs > 0)
            valid_actions.push to_action(ax, ay)
          end
        end
      end
      return valid_actions
    end

    # ある状態から行動し、次の状態と報酬を返す
    def step(state, action)
      x, y, vx, vy = to_position_speed(state)
      ax, ay = to_ax_ay(action)
      vx += ax
      vy += ay
      new_x = x + vx
      new_y = y + vy

      if course_info(new_x, new_y) == OUT
        next_state = to_state(x, y, vx, vy)
        reward = -5
      else
        next_state = to_state(new_x, new_y, vx, vy)
        reward = -1
      end

      return next_state, reward
    end

    private

    def to_state(x, y, vx, vy)
      [x, y, vx, vy].map(&:to_s).join(',')
    end

    def to_position_speed(state)
      state.split(',').map(&:to_i)
    end

    def to_position(state)
      to_position_speed(state).slice(0, 2)
    end

    def to_speed(state)
      to_position_speed(state).slice(2, 2)
    end

    def to_course_info(state)
      x, y = to_position(state)
      course_info(x, y)
    end

    def course_info(x, y)
      @course_info[y][x]
    end

    def to_action(ax, ay)
      [ax, ay].map(&:to_s).join(',')
    end

    def to_ax_ay(action)
      action.split(',').map(&:to_i)
    end

  end

end
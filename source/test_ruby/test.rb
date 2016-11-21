require './rental_car_problem'
require './status_value'
require './policy'
require 'awesome_print'

if __FILE__ == $PROGRAM_NAME
  include RentalCarProblem
  status_value = StatusValue.new
  ap status_value

end

from libs.rentalcar_problem.rental_car_problem import StatusValue, Policy, PolicyIterationMethod

if __name__ == '__main__':
    value = StatusValue()

    # print(value.poisson(1,2))

    policy = Policy()
    policy_iteration = PolicyIterationMethod(value=value, policy=policy, verbose=True)

    policy_iteration.execute()

    print("最適状態価値関数")
    policy_iteration.value.print()

    print("最適方策")
    policy_iteration.policy.print()

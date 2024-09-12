def run_tests(fn, tests):
    successful_test_cases = 0

    for i, (input_data, expected) in enumerate(tests):
        res = fn(*input_data) if isinstance(
            input_data, tuple) and len(input_data) > 1 else fn(input_data)

        if res == expected:
            successful_test_cases += 1
        else:
            print(f"Test case {i+1} failed:")
            print("* Input    ->", input_data)
            print("* Expected ->", expected)
            print("* Actual   ->", res)
            print("\n", "=" * 36, "\n")

    print(f"📦 {successful_test_cases}/{len(tests)} tests passed!")

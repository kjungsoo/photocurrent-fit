
# remove the following comment line after implementing
# it is just there to temporarily suppress a warning in the unimplemented function


# noinspection PyUnusedLocal
def compile_data(stopping_voltages, photocurrents):

    # We have two data arrays. The photocurrents are the independent (y) values. The stopping voltages
    # are the dependent (x) values.

    compiled_data = dict()
    counter = 0
    for voltage in stopping_voltages:
        current = photocurrents[counter]
        if voltage in compiled_data:
            i_sum, i_sum_2, i_count = compiled_data[voltage]
            i_sum += current
            i_sum_2 += current * current
            i_count += 1
            compiled_data[voltage] = i_sum, i_sum_2, i_count
        else:
            compiled_data[voltage] = current, current * current, 1
        counter += 1

    # These need to be compiled into a single dictionary whose keys are the x values and whose values are
    # tuples containing the sum of y values, the sum of the squares of the y values, and their count.

    return compiled_data

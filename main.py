import csv

def get_distinct_letter_len(sitter_name):
    parsed_set = set("".join(sitter_name.lower().split()))
    parsed_set.remove('.')
    return len(parsed_set)

def get_num_sitter_stays(sitter_email):
    d = {}
    for row in stored_csv:
        curr_sitter_email = row[10]

        if curr_sitter_email in d:
            d[curr_sitter_email] += 1
        else:
            d[curr_sitter_email] = 1
    
    return d[sitter_email]

def get_profile_score(distinct_letter_len):
    return 5 * (distinct_letter_len / 26)

def get_rating_score(sitter_email):
    # Correct for Paul S. (Rating score of 3.0 (i.e 21 / 7)) tested!
    d = {}
    for row in stored_csv:
        curr_sitter_email, curr_rating = row[10], row[0]

        if curr_sitter_email in d:
            d[curr_sitter_email] += int(curr_rating)
        else:
            d[curr_sitter_email] = int(curr_rating)

    return d[sitter_email] / get_num_sitter_stays(sitter_email)

def get_search_score(sitter_email, profile_score, rating_score):
    num_sitter_stays = get_num_sitter_stays(sitter_email)

    # What if the number of stays is between 1 - 9? Is it the avg of profile score and rating score?? (Ask)
    if num_sitter_stays == 0:
        return float(profile_score)
    
    elif num_sitter_stays >= 10:
        return float(rating_score)
    
    # IDK IF THIS IS HOW U ACTUALLY CALCULATE IT (WAIT FOR EMAIL REPLY)
    else:
        return (float(profile_score) + float(rating_score)) / 2

def populate_dict(local_stored_csv):
    '''
    Loop through each row in the csv
        Populate our dictionary with the sitter_email, sitter_name, profile_score, rating_score, and search_score
            profile_score - 5x fraction of distinct letters (use set) in sitter_name (5 * (distinct_len / 26))
            rating_score - avg of stay ratings
            search_score - weighted avg of profile_score and rating_score
                If sitter has no stays, search_score = profile_score
                If sitter >= 10 stays, search_score = rating_score

            Format scores to 2 decimal places
    '''
    list_of_sitters_d = []

    for row in local_stored_csv:
        sitters_email, sitters_name = row[10], row[6]
        distinct_letter_len = get_distinct_letter_len(sitters_name)
        
        if sitters_email not in list_of_sitters_d:
            profile_score = "{:.2f}".format(get_profile_score(distinct_letter_len))
            rating_score = "{:.2f}".format(get_rating_score(sitters_email))
            search_score = "{:.2f}".format(get_search_score(sitters_email, profile_score, rating_score))

            sitters_d = {"email": sitters_email, "name": sitters_name, "profile_score": profile_score, "rating_score": rating_score, "search_score": search_score}

            list_of_sitters_d.append(sitters_d)

    return list_of_sitters_d

def convert_to_csv_file(list_of_sitter_dicts):
    sitters_info = ['email', 'name', 'profile_score', 'rating_score', 'search_score']
    sorted_list_of_sitter_dicts = sorted(list_of_sitter_dicts, key = lambda x: (-float(x['search_score']), x['name']))
    
    with open('sitters.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = sitters_info)
        writer.writeheader()
        writer.writerows(sorted_list_of_sitter_dicts)

def store_csv(csvreader):
    csvfile_to_2D_list = []

    for row in csvreader:
        csvfile_to_2D_list.append(row)

    return csvfile_to_2D_list

if __name__ == "__main__":
    # TODO1: make sure to use command-line prompt for csv file (i.e we're just hardcoding it rn)
    # TODO2: test the search ranking algo

    file = open('reviews.csv')
    csvreader = csv.reader(file)
        
    header = next(csvreader)     # Skips the first row of csv

    stored_csv = store_csv(csvreader)
    list_of_sitter_dicts = populate_dict(stored_csv)
    convert_to_csv_file(list_of_sitter_dicts)

    file.close()

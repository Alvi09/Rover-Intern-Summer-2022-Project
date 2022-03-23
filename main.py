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

def populate_dict(local_stored_csv):
    '''
    Loop through each row in the csv
        Populate our dictionary with the sitter_email, sitter_name, profile_score, rating_score, and search_score
            profile_score - 5x fraction of distinct letters (use set) in sitter_name (5*6 or 5* (1/6))
            rating_score - avg of stay ratings
            search_score - weighted avg of profile_score and rating_score
                If sitter has no stays, search_score = profile_score
                If sitter >= 10 stays, search_score = rating_score

            Format scores to 2 decimal places
    '''
        
    sitters_list_of_d = []

    for row in local_stored_csv:
        sitters_email, sitters_name = row[10], row[6]
        distinct_letter_len = get_distinct_letter_len(sitters_name)
        
        if sitters_email in sitters_list_of_d:
            # Update scores?
            pass

        else:
            profile_score = 5 * (1 / distinct_letter_len)
            rating_score = 0
            search_score = 0

            num_sitter_stays = get_num_sitter_stays(sitters_email)
            sitters_d = {"email": sitters_email, "name": sitters_name, "profile_score": profile_score, "rating_score": rating_score, "search_score": search_score}

            sitters_list_of_d.append(sitters_d)

    print(sitters_d)

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
    populate_dict(stored_csv)

    file.close()
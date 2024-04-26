from bridges.color_grid import *
from bridges.bridges import *
from bridges.color import *
from bridges.data_src_dependent import data_source
import sys
import os

#will split list in half, sort, then merge back together
def merge_sort(names, start, end):
    if start < end:
        middle = start + (end - start) // 2

        #recursive call to sort both sub lists
        merge_sort(names, start, middle)
        merge_sort(names, middle + 1, end)
        vect1 = names[start:middle + 1] #first half of original list
        vect2 = names[middle + 1:end + 1] #second half of original list

        #initilizing beginning elements of sequences
        vect1_elem = 0
        vect2_elem = 0
        names_vect_elem = start

        #while not done finished with either sequence
        while vect1_elem < len(vect1) and vect2_elem < len(vect2):
            #checks if movie name of left sublist is alphabetically before right
            if vect1[vect1_elem].movie_name < vect2[vect2_elem].movie_name:
                #puts element into output sequence and continues thru list
                names[names_vect_elem] = vect1[vect1_elem]
                vect1_elem += 1
            else: #if the other movie name actually comes before
                names[names_vect_elem] = vect2[vect2_elem] #put that element into output sequence
                vect2_elem += 1
            names_vect_elem += 1

        #copy remaining items from first sequence to output sequence
        while vect1_elem < len(vect1):
            names[names_vect_elem] = vect1[vect1_elem]
            vect1_elem += 1
            names_vect_elem += 1

        #copy remaining items from second sequence to output sequence
        while vect2_elem < len(vect2):
            names[names_vect_elem] = vect2[vect2_elem]
            vect2_elem += 1
            names_vect_elem += 1

        return names

def main():

    bridges = Bridges(9, "enastevska", "690575246699")

    bridges.set_title ("Accessing Wikidata Movie/Actor Data")

    list  = data_source.get_wiki_data_actor_movie(1955, 1955)
    print ("Data Records in 1955: " + str(len(list)) + "\n")
    print ("First 3 records:\n")
    for i in range(3):
        print(str(i) + ")Actor-Movie Data:\n" +
             "\tMovie: " + list[i].movie_uri + ", " + list[i].movie_name + "\n" +
             "\tActor: " + list[i].actor_uri + ", " + list[i].actor_name + "\n")

    #merge sorting data by movie name
    merge_sort(list, 0, len(list) - 1)
    print("\nFirst 15 records sorted by movie name with merge sort:\n")
    for i in range(min(15, len(list))):  #prints first 15 movie names with merge sort algorithm
        print(f"{i}) Actor-Movie Data:\n\tMovie: {list[i].movie_uri}, {list[i].movie_name}\n"
              f"\tActor: {list[i].actor_uri}, {list[i].actor_name}\n")

    #built-in sort method to sort the list for comparison
    list.sort(key=lambda x: x.movie_name)
    print("\nFirst 15 records sorted by built-in sort method:\n")
    for i in range(min(25, len(list))):
        print(f"{i}) Actor-Movie Data:\n\tMovie: {list[i].movie_uri}, {list[i].movie_name}\n"
              f"\tActor: {list[i].actor_uri}, {list[i].actor_name}\n")

if __name__ == "__main__":
    main()
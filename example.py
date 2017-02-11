#!/usr/bin/env python

from rxlabel.rxlabel import RxLabel

API_KEY = 'LRhX4hpCq19DW27Xwgq1Rcm6DihSECaBldatSFmY'


def main():
    rx = RxLabel(api_key=API_KEY)
    result = rx.search_generic_name(search_term='ibuprofen')

    print result

if __name__ == '__main__':
    main()

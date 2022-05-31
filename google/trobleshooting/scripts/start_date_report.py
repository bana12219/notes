#!/usr/bin/env python3


import csv
import datetime
import requests


FILE_URL = "https://storage.googleapis.com/gwg-hol-assets/gic215/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""
    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()
    return datetime.datetime(year, month, day)

def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""
    # Download the file over the internet
    response = requests.get(url, stream=True)
    lines = []
    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines

def get_same_or_newer(start_date):
    """Returns the employees that started on the given date, or the closest one."""
    data = get_file_lines(FILE_URL)
    # hasta aqui leo la fecha, y obtengo el archivo de datos (stream)
    reader = csv.reader(data[1:])  #lo leo
    emps_by_date=dict()
    for row in reader: 
        name,surname,department,empstartdate=row
        row_date = datetime.datetime.strptime(empstartdate, '%Y-%m-%d')
        # If this date is smaller than the one we're looking for,
        # we skip this row
        if row_date < start_date:
            continue
        #devuelve la lista de empleados dados de alta en esa fecha, si no una lista vacia y le agrega el registro
        empls=emps_by_date.get(row_date,list())
        empls.append ("{} {}".format(name,surname))
        #actualiza el registro
        emps_by_date[row_date]=empls

    return emps_by_date



def list_newer(start_date):
    # el objetivo es imprimir los empleados ordenados por fecha de ingreso a partir de la fecha dada
    if not start_date > datetime.datetime.today():
        for start_date, employees  in get_same_or_newer(start_date):
        print("Started on {}: {}".format(start_date.strftime("%b %d, %Y"), employees))
        # Now move the date to the next one
        start_date = start_date + datetime.timedelta(days=1)

def main():
    start_date = get_start_date()
    list_newer(start_date)

if __name__ == "__main__":
    main()

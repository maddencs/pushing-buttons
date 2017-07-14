"""
Script for running on Raspberry Pi
"""
import requests
from gpiozero import Button

API_URL = '<base_url>/push-button'

red_button = Button(26)
blue_button = Button(19)
red_button_url = API_URL + '?color=red'
blue_button_url = API_URL + '?color=blue'


def watch_buttons():
    while True:
        if red_button.is_pressed:
            requests.get(red_button_url)
        if blue_button.is_pressed:
            requests.get(blue_button_url)


if __name__ == '__main__':
    watch_buttons()

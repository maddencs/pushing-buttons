"""
Script for running on Raspberry Pi
"""
from time import sleep
import requests
from gpiozero import Button

API_URL = 'http://10.0.0.176:8001/buttons/push-button'

red_button = Button(26)
blue_button = Button(19)
red_button_url = API_URL + '?color=red'
blue_button_url = API_URL + '?color=blue'


def watch_buttons():
    while True:
        if red_button.is_pressed:
            requests.get(red_button_url)
            while red_button.is_pressed:
                continue
            sleep(.3)
            break
        if blue_button.is_pressed:
            requests.get(blue_button_url)
            while blue_button.is_pressed:
                continue
            sleep(.3)
            break
    watch_buttons()


if __name__ == '__main__':
    watch_buttons()

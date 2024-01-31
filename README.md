### install
``` shell
$ sudo apt-get -y install v4l-utils
```

``` shell
$ poetry install
```

### find device
``` shell
$ v4l2-ctl --list-devices
```
```
HD USB Camera: HD USB Camera (usb-0000:00:14.0-3.4):
        /dev/video8
        /dev/video9
        /dev/media3

HK 1080P K20Pro: HK 1080P K20Pr (usb-0000:00:14.0-4.4):
        /dev/video6
        /dev/video7
        /dev/media2

Intel(R) RealSense(TM) Depth Ca (usb-0000:00:14.0-7.3):
        /dev/video0
        /dev/video1
        /dev/video2
        /dev/video3
        /dev/video4
        /dev/video5
        /dev/media0
        /dev/media1
```



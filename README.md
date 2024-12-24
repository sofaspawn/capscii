## Capscii
- ASCII representation of camera feed (starting with random images)

## current status:
<div style="display: flex; justify-content: space-between;">
    <img src="./megumi.jpg" alt="test_image" width="45%" />
    <img src="./demo.png" alt="pixelated image" width="45%" />
</div>

## Problems:
- too slow for any real use case
- not optimized
- image dimensions are messed up

## Potential solutions:
- implement the same in C/rust or similarly performant language
- or be happy with the current state

## TODO:
- [x] load images
- [x] get brightness value of each pixel. (used weighted luminosity values)
- [x] map brightness value to ascii character
- [x] display ascii character in terminal

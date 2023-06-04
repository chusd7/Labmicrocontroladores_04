Esta carpeta se debe copiar a la carpeta de ejemplos de libopencm3-examples.

Una vez ahi, se procede con la ejecución del script de python telemetry.py.

En caso de requerir algún cambio en el archivo del giroscopio spi-mems, se debe ejecutar los siguientes comandos en la terminal:

- make - para generar el .elf
- arm-none-eabi-objcopy -O binary spi-mems.elf spi-mems.bin - para cambiar de .elf a .bin
- st-flash write spi-mems.bin 0x08000000 - para subirle el código a la tarjeta STM32F429I-Discovery

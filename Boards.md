## Compliance Criteria for Boards

See [Release versions](https://github.com/ARMmbed/mbed-enabled-requirements/releases).

All Mbed Enabled products must meet all MUST compliance criteria and are encouraged to meet all SHOULD compliance criteria. 

This applies to development or evaluation boards that include a Target MCU and an Interface. 

* [B-CC-1] MUST implement all functionality against the current Mbed OS major release (see [technical requirements for Boards](#technical-requirements))
* [B-CC-2] MUST pass all Mbed OS functional and system validation tests for the current Mbed OS major release.
* [B-CC-3] MUST have the support software merged mainline in the [official Mbed OS repository](https://github.com/ARMmbed/mbed-os/) according to porting and [contributor](https://os.mbed.com/contributing/) guidelines.
* [B-CC-4] MUST provide comprehensive examples for key features and functionality
* [B-CC-5] SHOULD use supported Components
* [B-CC-6] MUST have an Mbed Enabled Interface circuit and firmware available (see Mbed Enabled compliance criteria for [Interfaces](./Interfaces.md))
* [B-CC-7] MUST have a pinout diagram based on the [Mbed pinout template](./resources/mbed-Pinout-template.pptx)
* [B-CC-8] MUST provide product photo, description, features and other marketing collateral
* [B-CC-9] MUST have technical documents available for download from the Mbed website
* [B-CC-10] MUST have EDA consumable files available for download from the Mbed website
* [B-CC-11] MUST have a support engineer to respond to [Github issues](https://github.com/ARMmbed/mbed-os/issues) in a timeline manner
* [B-CC-12] MUST have a support engineer reviewing the [Mbed Forums](https://forums.mbed.com/) to monitor community questions or feedback regarding the product
* [B-CC-13] MUST provide 5x units mounted on a PCB for validation and regression testing.
* [B-CC-14] MUST have a license on the source-code identifiable using SPDX compatible with Mbed OS license on Github
## Technical Requirements

All Mbed Enabled products must pass the test defined by these technical requirements.

This applies to development or evaluation boards that include both a Target MCU and an Interface.

### Class: Baseline

This set of requirements aims at constrained and maintream devices.

* [B-TG] Target MCU support Files
    * [B-TG-1] MUST provide folder structure as per the Mbed OS [specification](https://os.mbed.com/docs/mbed-os/latest/porting/porting-targets.html)
* [B-M1] Microcontroller requirements: Baseline
    *	[B-M1-1] MUST implement ARMv6-M, ARMv7-M, ARMv8-M or newer Arm architecture.
    *	[B-M1-2] MUST provide at least 16KB RAM and 64KB Flash.
* [B-CM] CMSIS-CORE
    * [B-CM-1] MUST provide CMSIS-CORE implementation as per [template](https://www.keil.com/pack/doc/CMSIS/Core/html/templates_pg.html), start-up files and linker scripts for toolchains.
* [B-BM] Baremetal profile
   * [B-BM-1] MUST capable of using using the baremetal profile. See [Mbed OS 6 bare metal porting guide](https://os.mbed.com/docs/mbed-os/latest/bare-metal/porting-a-target-from-mbed-os-2-to-mbed-os-6-bare-metal.html).
* [B-TM] TIMERS
    * [B-TM-1] MUST provide precise timing resource. See [specification, porting & testing guide](https://os.mbed.com/docs/latest/porting/microsecond-ticker.html)
    * [B-TM-2] MUST implement low power timing resource if provided by hardware. See [specification, porting & testing guide](https://os.mbed.com/docs/latest/porting/low-power-ticker.html)
    * [B-TM-3] MUST implement sleep API. See [specification, porting & testing guide](https://os.mbed.com/docs/latest/porting/sleep.html)
    * [B-TM-4] MUST provide Tickless support. See [porting & testing guide](https://os.mbed.com/docs/mbed-os/latest/porting/tickless-mode.html)
    * [B-TM-5] SHOULD implement watchdog API if provided by MCU. See [specification, porting & testing guide](https://os.mbed.com/docs/latest/porting/watchdog-port.html)
* [B-H] Drivers
    * [B-HG-1] MUST implement dynamic GPIO configuration. See [porting & testing guide](https://os.mbed.com/docs/mbed-os/latest/porting/gpio.html)
    * [B-HG-2] SHOULD implement static GPIO configuration. See [porting & testing guide](https://os.mbed.com/docs/mbed-os/latest/porting/static-pinmap-port.html)
    * [B-HU-1] MUST implement UART/Serial. See [porting & testing guide](https://os.mbed.com/docs/latest/porting/serial-port.html)
    * [B-HC-1] MUST implement I2C if provided by MCU. See [porting & testing guide](https://os.mbed.com/docs/mbed-os/latest/porting/i2c-port.html)
    * [B-HS-1] MUST implement SPI Master and SHOULD implement SPI Slave if provided by MCU. See [porting & testing guide](https://os.mbed.com/docs/mbed-os/latest/porting/spi-port.html)
    * [B-HQ-1] MUST implement QuadSPI Master if provided by SoC. See [porting & testing guide](https://os.mbed.com/docs/mbed-os/latest/porting/quadspi-port.html)
    * [B-HA-1] MUST implement [AnalogIn](https://github.com/ARMmbed/mbed-os/blob/master/hal/include/hal/analogin_api.h) and [AnalogOut](https://github.com/ARMmbed/mbed-os/blob/master/hal/include/hal/analogout_api.h) if provided by the MCU
    * [B-HP-1] MUST implement [PWM](https://github.com/ARMmbed/mbed-os/blob/master/hal/include/hal/pwmout_api.h) if provided by the MCU
    * [B-HF-1] SHOULD pass [FPGA shield tests](https://github.com/ARMmbed/mbed-os/tree/master/hal/tests/TESTS/mbed_hal_fpga_ci_test_shield) for peripheral drivers
* [B-STD-CON] Support for standard pin-names and connectors
    * [B-STD-CON1] SHOULD support common pin-names for LED/BUTTONs and UART over [interface](./Interfaces.md) to PC. See [porting guide](https://github.com/ARMmbed/mbed-os-5-docs/pull/1417/files)
    * [B-STD-CON2] SHOULD support the Arduino UNO standard if the board has a connector compliant. See [porting guide](https://github.com/ARMmbed/mbed-os-5-docs/pull/1417/files)
* [B-RC] RTC
    * [B-RC-1] MUST implement RTC support if provided by MCU or board. See [porting & testing guide](https://os.mbed.com/docs/mbed-os/latest/porting/rtc-port.html)
* [B-ES] Entropy source / TRNG
   * [B-ES-1] MUST implement hardware entropy source support if provided by the MCU. See [porting & testing guide](https://os.mbed.com/docs/mbed-os/latest/porting/entropy-sources.html)
* [B-CR] Hardware Cryptography
    * [B-CR-1] MUST implement hardware cryptography acceleration functionality if provided by the MCU or board, and TFM is not available. See [porting & testing guide](https://os.mbed.com/docs/mbed-os/latest/porting/hardware-accelerated-crypto.html)
* [B-TFM]
    * [B-TFM-1] SHOULD support TFM for Mbed OS if using v7-M (dual core) or v8-M MCU. See [porting guide & testing guide](https://os.mbed.com/docs/mbed-os/latest/porting/porting-security.html)
* [B-CRC]
    * [B-CRC-1] MUST implement hardware CRC if provided by hardware. See [porting & testing guide](https://os.mbed.com/docs/latest/porting/hardware-crc.html)
* [B-TC] Toolchain Compilers - see supported [toolchain versions](https://os.mbed.com/docs/mbed-os/latest/tools/index.html) in Mbed OS
    * [B-TC-1] MUST support GCC for Arm architecture
    * [B-TC-2] MUST support Arm Compiler 6
* [B-CMK] Support for Cmake and Mbed CLI 2
    * [B-CMK-1] MUST support compilation of a target using Cmake through Mbed CLI 2. See [user](https://os.mbed.com/docs/mbed-os/latest/build-tools/use.html) and [porting guide](https://github.com/ARMmbed/mbed-os-5-docs/blob/development/docs/porting/target/cmake.md)
* [B-IDE] Support for Online and Desktop IDEs
    * [B-IDE-1] MUST support the latest version of [Mbed Studio](https://os.mbed.com/studio/) to compile and deploy applications to the board
    * [B-IDE-1] SHOULD support debugging the board by providing the required CMSIS-Pack containing SVD definitions. See [porting guide](https://os.mbed.com/docs/mbed-studio/current/monitor-debug/enabling-debugging-for-unsupported-boards.html)

### Class: Advanced

This set of requirements builds on top of Baseline and aims at mainstream devices.

* [B-M2] Microcontroller requirements: Advanced
   * [B-M2-1] MUST implement ARMv7-M, ARMv8-M or newer Arm architecture
   * [B-M2-2] MUST provide at least 64KB RAM and 256KB Flash
* [B-RT] RTOS profile
   * [B-RT-1] MUST have RTOS enabled and be capable of using threads. See [Mbed RTOS tests](https://github.com/ARMmbed/mbed-os/tree/master/rtos/tests/TESTS/mbed_rtos).
* [B-EH] Extended HAL
   * [B-EH-1] MUST implement Mbed OS Flash HAL and Mbed OS Flash IAP functionality See [porting & testing guide](https://os.mbed.com/docs/latest/porting/flash.html)
   * [B-EH-2] SHOULD implement ResetReason API if provided by the MCU. See [specification, porting & testing guide](https://os.mbed.com/docs/latest/porting/resetreason-port.html)
* [B-ST] Storage
   * [M-ST-1] MUST provide storage and implement BlockDevice driver if provided by hardware. See [specification & porting](https://os.mbed.com/docs/latest/porting/porting-storage.html)
   * [M-ST-2] MUST pass all BlockDevice and Filesystem tests. See [documentation & testing guide](https://os.mbed.com/docs/mbed-os/latest/porting/blockdevice-port.html)
* [B-BT] Non-IP Connectivity - Bluetooth Low Energy
  * [B-BT-1] MUST implement a BLE HCI driver for Cordio BLE stack, and functionality covering the BLE controller capabilities in compliance with BLE 5.2 specification.
  * [B-BT-2] MUST pass the BLE integration [tests](https://github.com/ARMmbed/mbed-os-bluetooth-integration-testsuite). See [porting & testing guide](https://github.com/ARMmbed/mbed-os/blob/master/connectivity/FEATURE_BLE/source/cordio/)
* [B-ET] IP Connectivity - Ethernet (IPv4 & IPv6)
  * [B-ET-1] MUST implement Mbed OS EMAC driver if provided by hardware. See [porting & testing guide](https://os.mbed.com/docs/latest/porting/ethernet-port.html)
  * [B-ET-2] MUST pass all Mbed OS Network Socket API tests. See [documentation & testing guide](https://os.mbed.com/docs/latest/porting/networkstack.html)
* [B-WF] IP Connectivity - WiFI (IPv4 & IPv6)
  * [B-WF-1] MUST implement Mbed OS EMAC driver if provided by hardware. See [porting & testing guide](https://os.mbed.com/docs/mbed-os/latest/porting/wifi-port.html)
  * [B-WF-2] MUST pass all Mbed OS Network Socket API tests. See [documentation & testing guide](https://os.mbed.com/docs/latest/porting/networkstack.html)
* [B-CL] IP Connectivity - Cellular
  * [B-CL-1] MUST implement Mbed OS CellularInterface driver for either PPP or AT mode if provided by hardware. See [porting & testing guide](https://os.mbed.com/docs/mbed-os/latest/porting/cellular-device-porting.html)
  * [B-CL-2] MUST pass all Mbed OS Network Socket API tests. See [documentation & testing guide](https://os.mbed.com/docs/latest/porting/networkstack.html)
* [B-SY] Integration and stress tests. See [testing guide](https://os.mbed.com/docs/mbed-os/latest/porting/integration-tests.html)
  * [B-IT-1] MUST pass all storage and multithreaded stress tests if storage is provided. 
  * [B- IT -2] MUST pass all network and multithreaded stress tests if IP connectivity is provided
  * [B- IT-3] MUST pass all combined stress tests if both storage and IP connectivity is provided

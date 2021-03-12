## Compliance Criteria for Components

See [Release versions](https://github.com/ARMmbed/mbed-enabled-requirements/releases).

All Mbed Enabled products must meet all MUST compliance criteria and are encouraged to meet all SHOULD compliance criteria. 

This applies to all components.

* [C-CC-1] MUST implement all functionality against the current Mbed OS major release (see [technical requirements for Components](#technical-requirements)).
* [C-CC-2] MUST pass all Mbed OS functional and system validation tests for the current Mbed OS major release.
* [C-CC-3] MUST have the support software available on a public website.
* [C-CC-4] SHOULD support all additional connectivity protocols that are available.
* [C-CC-5] MUST provide comprehensive examples for key component features and functionality.
* [C-CC-6] MUST test the component and its functionality against 3 Mbed Enabled boards.
* [C-CC-7] SHOULD test the component and its functionality against 10 Mbed Enabled boards.
* [C-CC-8] MUST have a pinout diagram based on the [Mbed pinout template](./resources/mbed-Pinout-template.pptx)
* [C-CC-9] MUST provide product photo, description, features and other marketing collateral.
* [C-CC-10] MUST have technical documents available for download from the Mbed website.
* [C-CC-11] MUST have EDA consumable files available for download from the Mbed website.
* [C-CC-12] MUST have a public issue tracker and feedback mechanism.
* [C-CC-13] MUST have a support engineer reviewing the [Mbed Forums](https://forums.mbed.com/) to monitor community questions or feedback regarding the product
* [C-CC-14] MUST provide 5 units for validation and regression testing.
* [C-CC-15] MUST have a license identifiable using SPDX.

## Technical Requirements

All Mbed Enabled products must pass the test defined by these technical requirements.
This applies to development or evaluation components.

* [C-DR] Component Drivers
    * [C-DR-1] MUST provide driver libraries for all hardware elements available on the component. Libraries must be publicly available.
    * [C-DR-2] MUST use Mbed OS Driver APIs for peripheral GPIO, SPI, I2C, UART, AnalogIn, PWM functionality.
* [C-TC] Toolchain Compilers - see supported [toolchain versions](https://os.mbed.com/docs/mbed-os/latest/tools/index.html) in Mbed OS
    * [C-DR-1] MUST support GCC for Arm architecture
    * [C-DR-2] MUST support Arm Compiler 6
* [C-ST] Storage
   * [C-ST-1] MUST provide storage and implement BlockDevice driver if provided by hardware. See [specification & porting guide](https://os.mbed.com/docs/mbed-os/latest/porting/porting-storage.html).
* [C-BT] Non-IP Connectivity - Bluetooth Low Energy
  * [C-BT-1] MUST implement a BLE HCI driver for Cordio BLE stack, and functionality covering the BLE controller capabilities in compliance with BLE 5.2 specification.
  * [C-BT-2] MUST pass the BLE integration [tests](https://github.com/ARMmbed/mbed-os-bluetooth-integration-testsuite). See [porting & testing guide](https://github.com/ARMmbed/mbed-os/blob/master/connectivity/FEATURE_BLE/source/cordio/)
* [C-ET] IP Connectivity - Ethernet (IPv4 & IPv6)
   * [C-ET-1] MUST implement Mbed OS EMAC driver if provided by hardware. See [porting & testing guide](https://os.mbed.com/docs/latest/porting/ethernet-port.html)
   * [C-ET-2] MUST pass all Mbed OS Network Socket API tests. See [documentation & testing guide](https://os.mbed.com/docs/latest/porting/networkstack.html)
* [C-WF] IP Connectivity - WiFI (IPv4 & IPv6)
  * [C-WF-1] MUST implement Mbed OS EMAC driver if provided by hardware. See [porting & testing guide](https://os.mbed.com/docs/mbed-os/latest/porting/wifi-port.html)
  * [C-WF-2] MUST pass all Mbed OS Network Socket API tests. See[documentation & testing guide](https://os.mbed.com/docs/latest/porting/networkstack.html)
* [C-CL] IP Connectivity - Cellular
  * [C-CL-1] MUST implement Mbed OS CellularInterface driver for either PPP or AT mode if provided by hardware. See [porting & testing guide](https://os.mbed.com/docs/mbed-os/latest/porting/cellular-device-porting.html)
  * [C-CL-2] MUST pass all Mbed OS Network Socket API tests. See [documentation & testing guide](https://os.mbed.com/docs/latest/porting/networkstack.html)
* [C-SY] Integration and stress tests. See [testing guide](https://os.mbed.com/docs/mbed-os/latest/porting/integration-tests.html)
  * [C-IT-1] MUST pass all storage and multithreaded stress tests if storage is provided.
  * [C- IT -2] MUST pass all network and multithreaded stress tests if IP connectivity is provided
  * [C- IT-3] MUST pass all combined stress tests if both storage and IP connectivity is provided

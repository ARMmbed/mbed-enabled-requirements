## Compliance Criteria for Interfaces

See [Release versions](https://github.com/ARMmbed/mbed-enabled-requirements/releases).

All Mbed Enabled products must meet all MUST compliance criteria and are encouraged to meet all SHOULD compliance criteria. 

* [I-CC-1] MUST have technical documents available for download from the Mbed Developer website. 
* [I-CC-2] MUST have EDA consumable files available for download from the Mbed Developer website. 
* [I-CC-3] MUST have a support engineer on the Mbed Developer website to monitor community questions/feedback regarding the product and supporting software. 
* [I-CC-4] MUST provide 10x units for validation and regression testing. 
* [I-CC-6] MUST have product specification document publicly available, e.g. https://github.com/ARMmbed/DAPLink 
* [I-CC-7] MUST have a schematic publicly available 
* [I-CC-8] MUST have the support software for boards merged mainline in the official Mbed OS repository https://github.com/ARMmbed/mbed-os 
* [I-CC-9] MUST have a public issue tracker and feedback mechanism, e.g. https://github.com/ARMmbed/DAPLink/issues 

## Technical Requirements

* [I-OS] Operating Systems 
  * [I-OS-1] MUST be compatible with all actively supported versions of Windows 10, macOS Big Sur 11 and Linux Ubuntu 20.04 LTS operating systems.
* [I-FS] USB Filesystem 
  * [I-FS-1] MUST implement USB mass storage device (MSD) support that is capable of programming the target's microcontroller memory system (usually flash). 
  * [I-FS-2] MUST support programming binary files. 
  * [I-FS-3] SHOULD support programming hex files. 
  * [I-FS-4] MUST support programming only the region specified by the file. 
  * [I-FS-5] MUST indicate both success and failure programming status. 
  * [I-FS-6] MUST have a method for reading the contents of target microcontroller memory system (usually flash). 
  * [I-FS-7] MUST contain a read-only HTML-5 compliant mbed.htm file containing URL that redirects to the mbed.com product specific page. 
  * [I-FS-8] MUST have a “details.txt” file containing board ID and circuit ID. 
* [I-VC] USB Virtual COM Port 
  * [I-VC-1] MUST implement USB communication device class (CDC) which exposes target microcontroller UART transmit and receive pin. 
  * [I-VC-2] MUST support the target microcontroller changing speed baud rates 2400, 9600, ..., 115200. 
  * [I-VC-3] SHOULD support all standard baud-rates 2400 thru 921600. 
  * [I-VC-4] MUST support ACM 'Send Break' resulting in target microcontroller reset sequence. 
  * [I-VC-5] SHOULD provide a user indication in case of a UART buffer overflow. 
* [I-DB] USB Debug 
  * [I-DB-1] MUST implement functionality that allows programming and debugging from the host PC. 
  * [I-DB-2] SHOULD be CMSIS-DAPv2. 
  * [I-DB-3] SHOULD support WebUSB.
  * [I-DB-4] SHOULD support pyOCD through CMSIS-Packs.

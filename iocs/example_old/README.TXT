mks937a example - Pete Owens 11-9-2003
    Example to illustrate use of the mks937a application 

Hardware setup:
VME 64x Crate:
Slot 1: IOC - PPC 604
Slot 4: Hytec 8002 IP Carrier 8002 card -
    Slot C: Hytec 8401 ADC
        Signal 0: Combination Gauge CC/B1: TS-VA-GAUGE-01
        Signal 1: Combination Gauge  A/B2: TS-VA-GAUGE-02
Slot 8: Hytec 8002 IP Carrier 8002 card -
    Slot B: Hytec 8515 Octal serial module -
        Port 0: /ty/71/1 - connected to MKS 937A controller
            Channel CC (1): TS-VA-IMG-01
            Channel A  (2): TS-VA-IMG-02
            Channel B1 (4): TS-VA-PIRG-01
            Channel B2 (5): TS-VA-PIRG-02

This directory contains following files:
    st.cmd             - VxWorks startup script to initialise an IOC
    mks937a.sub        - substitution files to instantiate the records
    mks937a-launch.edl - EDM pannel to launch panels for the conected gauges 
    startgui           - script to start off the user interface







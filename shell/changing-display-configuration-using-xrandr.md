# Changing Display Configuration using xrandr

1. To list available displays

   ```bash
   xrandr -q
   ```

   Sample output

   ```bash
   Screen 0: minimum 320 x 200, current 2560 x 1080, maximum 16384 x 16384
   eDP connected primary 1920x1080+0+0 (normal left inverted right x axis y axis) 309mm x 173mm
      1920x1080     60.01*+
      1680x1050     60.01  
      1280x1024     60.01  
      1440x900      60.01  
      1280x800      60.01  
      1280x720      60.01  
      1024x768      60.01  
      800x600       60.01  
      640x480       60.01  
   HDMI-A-0 connected 640x480+1920+0 (normal left inverted right x axis y axis) 0mm x 0mm
      640x480       59.94*
      1920x1080     60.01  
      1680x1050     60.01  
   DisplayPort-0 disconnected (normal left inverted right x axis y axis)
   ```

2. Add new resolution mode to display X.

   ```bash
   xrandr --addmode X 1280x1024
   ```

3. Use newly added mode.

   ```bash
   xrandr --auto --output X --mode 1280x1024
   ```

## Find mode Configuration

1. Using `gtf`

   ```bash
   gtf 1920 1080 60
   ```

   Sample output

   ```bash
     # 1920x1080 @ 60.00 Hz (GTF) hsync: 67.08 kHz; pclk: 172.80 MHz
     Modeline "1920x1080_60.00"  172.80  1920 2040 2248 2576  1080 1081 1084 1118  -HSync +Vsync
   ```

2. Using `cvt`

   ```bash
   cvt 800 600
   ```

   Sample output

   ```bash
   # 800x600 59.86 Hz (CVT 0.48M3) hsync: 37.35 kHz; pclk: 38.25 MHz
   Modeline "800x600_60.00"   38.25  800 832 912 1024  600 603 607 624 -hsync +vsync
   ```

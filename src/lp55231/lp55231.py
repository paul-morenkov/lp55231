from i2cdevice import BitField, Device, Register
from telemetrix.telemetrix import Telemetrix

dev = Device(
    0x32,
    registers=(
        Register(
            "CNTRL1",
            0x00,
            fields=(
                BitField("enable", 0b01000000),
                BitField("engine1_exec", 0b00110000),
                BitField("engine2_exec", 0b00001100),
                BitField("engine3_exec", 0b00000011),
            ),
        ),
        Register(
            "CNTRL2",
            0x01,
            fields=(
                BitField("engine1_mode", 0b00110000),
                BitField("engine2_mode", 0b00001100),
                BitField("engine3_mode", 0b00000011),
            ),
        ),
        Register("RATIO_MSB", 0x02, fields=(BitField("d9_ratio_en", 0b00000001))),
        Register(
            "RATIO_LSB",
            0x03,
            fields=(
                BitField("d8_ratio_en", 0b10000000),
                BitField("d7_ratio_en", 0b01000000),
                BitField("d6_ratio_en", 0b00100000),
                BitField("d5_ratio_en", 0b00010000),
                BitField("d4_ratio_en", 0b00001000),
                BitField("d3_ratio_en", 0b00000100),
                BitField("d2_ratio_en", 0b00000010),
                BitField("d1_ratio_en", 0b00000001),
            ),
        ),
        Register("OUTPUT_ONOFF_MSB", 0x04, fields=(BitField("d9_on", 0b00000001))),
        Register(
            "OUTPUT_ONOFF_LSB",
            0x05,
            fields=(
                BitField("d8_on", 0b10000000),
                BitField("d7_on", 0b01000000),
                BitField("d6_on", 0b00100000),
                BitField("d5_on", 0b00010000),
                BitField("d4_on", 0b00001000),
                BitField("d3_on", 0b00000100),
                BitField("d2_on", 0b00000010),
                BitField("d1_on", 0b00000001),
            ),
        ),
        Register(
            "D1_CTRL",
            0x06,
            fields=(
                BitField("mapping", 0b11000000),
                BitField("log_en", 0b00100000),
                BitField("temp_comp", 0b00011111),
            ),
        ),
        Register(
            "D2_CTRL",
            0x07,
            fields=(
                BitField("mapping", 0b11000000),
                BitField("log_en", 0b00100000),
                BitField("temp_comp", 0b00011111),
            ),
        ),
        Register(
            "D3_CTRL",
            0x08,
            fields=(
                BitField("mapping", 0b11000000),
                BitField("log_en", 0b00100000),
                BitField("temp_comp", 0b00011111),
            ),
        ),
        Register(
            "D4_CTRL",
            0x09,
            fields=(
                BitField("mapping", 0b11000000),
                BitField("log_en", 0b00100000),
                BitField("temp_comp", 0b00011111),
            ),
        ),
        Register(
            "D5_CTRL",
            0x0A,
            fields=(
                BitField("mapping", 0b11000000),
                BitField("log_en", 0b00100000),
                BitField("temp_comp", 0b00011111),
            ),
        ),
        Register(
            "D6_CTRL",
            0x0B,
            fields=(
                BitField("mapping", 0b11000000),
                BitField("log_en", 0b00100000),
                BitField("temp_comp", 0b00011111),
            ),
        ),
        Register(
            "D7_CTRL",
            0x0C,
            fields=(
                BitField("mapping", 0b11000000),
                BitField("log_en", 0b00100000),
                BitField("temp_comp", 0b00011111),
            ),
        ),
        Register(
            "D8_CTRL",
            0x0D,
            fields=(
                BitField("mapping", 0b11000000),
                BitField("log_en", 0b00100000),
                BitField("temp_comp", 0b00011111),
            ),
        ),
        Register(
            "D9_CTRL",
            0x0E,
            fields=(
                BitField("mapping", 0b11000000),
                BitField("log_en", 0b00100000),
                BitField("temp_comp", 0b00011111),
            ),
        ),
        # 0F to 15 reserved
        Register("D1_PWM", 0x16, fields=(BitField("pwm", 0xFF))),
        Register("D2_PWM", 0x17, fields=(BitField("pwm", 0xFF))),
        Register("D3_PWM", 0x18, fields=(BitField("pwm", 0xFF))),
        Register("D4_PWM", 0x19, fields=(BitField("pwm", 0xFF))),
        Register("D5_PWM", 0x1A, fields=(BitField("pwm", 0xFF))),
        Register("D6_PWM", 0x1B, fields=(BitField("pwm", 0xFF))),
        Register("D7_PWM", 0x1C, fields=(BitField("pwm", 0xFF))),
        Register("D8_PWM", 0x1D, fields=(BitField("pwm", 0xFF))),
        Register("D9_PWM", 0x1E, fields=(BitField("pwm", 0xFF))),
        # 1F to 25 reserved
        Register("D1_I_CTL", 0x26, fields=(BitField("current", 0xFF))),
        Register("D2_I_CTL", 0x27, fields=(BitField("current", 0xFF))),
        Register("D3_I_CTL", 0x28, fields=(BitField("current", 0xFF))),
        Register("D4_I_CTL", 0x29, fields=(BitField("current", 0xFF))),
        Register("D5_I_CTL", 0x2A, fields=(BitField("current", 0xFF))),
        Register("D6_I_CTL", 0x2B, fields=(BitField("current", 0xFF))),
        Register("D7_I_CTL", 0x2C, fields=(BitField("current", 0xFF))),
        Register("D8_I_CTL", 0x2D, fields=(BitField("current", 0xFF))),
        Register("D9_I_CTL", 0x2E, fields=(BitField("current", 0xFF))),
        # 2F to 35 reserved
        Register(
            "MISC",
            0x36,
            fields=(
                BitField("var_d_sel", 0b10000000),
                BitField("en_auto_incr", 0b01000000),
                BitField("powersave_en", 0b00100000),
                BitField("cp_mode", 0b00011000),
                BitField("pwm_ps_en", 0b00000100),
                BitField("clk_det_en", 0b00000010),
                BitField("int_clk_en", 0b00000001),
            ),
        ),
        Register("PC1", 0x37, fields=(BitField("pc", 0b01111111))),
        Register("PC2", 0x38, fields=(BitField("pc", 0b01111111))),
        Register("PC3", 0x39, fields=(BitField("pc", 0b01111111))),
        Register(
            "STATUS_IRQ",
            0x3A,
            fields=(
                BitField("ledtest_meas_done", 0b10000000),
                BitField("mask_busy", 0b01000000),
                BitField("startup_busy", 0b00100000),
                BitField("engine_busy", 0b00010000),
                BitField("ext_clk_used", 0b00001000),
                BitField("eng1_int", 0b00000100),
                BitField("eng2_int", 0b00000010),
                BitField("eng3_int", 0b00000001),
            ),
            read_only=True,
        ),
        Register(
            "INT_GPIO",
            0x3B,
            fields=(BitField("int_conf", 0b00000100), BitField("int_gpo", 0b00000001)),
        ),
        Register("GLOBAL_VAR", 0x3C, fields=(BitField("variable", 0xFF))),
        Register("RESET", 0x3D, fields=(BitField("reset", 0xFF))),
        Register(
            "TMP_CTL",
            0x3E,
            fields=(
                BitField("temp_meas_busy", 0b10000000, read_only=True),
                BitField("en_sensor", 0b00000100),
                BitField("cont_conv", 0b00000010),
                BitField("sel_ext_temp", 0b00000001),
            ),
        ),
        Register("TEMP_READ", 0x3F, fields=(BitField("temp", 0xFF)), read_only=True),
        Register("TEMP_WRITE", 0x40, fields=(BitField("temp", 0xFF))),
        Register(
            "TEST_CTL",
            0x41,
            fields=(
                BitField("en_test_adc", 0b10000000),
                BitField("en_test_int", 0b01000000),
                BitField("cont_conv", 0b00100000),
                BitField("test_ctrl", 0b00011111),
            ),
        ),
        Register("TEST_ADC", 0x42, fields=(BitField("test_adc", 0xFF)), read_only=True),
        # 43-44 reserved
        Register(
            "ENG_A_VAR", 0x45, fields=(BitField("variable", 0xFF)), read_only=True
        ),
        Register(
            "ENG_B_VAR", 0x46, fields=(BitField("variable", 0xFF)), read_only=True
        ),
        Register(
            "ENG_C_VAR", 0x47, fields=(BitField("variable", 0xFF)), read_only=True
        ),
        Register("MASTER_FADE_1", 0x48, fields=(BitField("fader", 0xFF))),
        Register("MASTER_FADE_2", 0x49, fields=(BitField("fader", 0xFF))),
        Register("MASTER_FADE_3", 0x4A, fields=(BitField("fader", 0xFF))),
        # 4B reserved
        Register("PROG1_START", 0x4C, fields=(BitField("addr", 0b01111111))),
        Register("PROG2_START", 0x4D, fields=(BitField("addr", 0b01111111))),
        Register("PROG3_START", 0x4E, fields=(BitField("addr", 0b01111111))),
        Register("PROG_PAGE_SEL", 0x4F, fields=(BitField("page_sel", 0b00000111))),
        # FIXME:
        Register("PROG_MEM_BASE", 0x50, fields=()),
        Register("PROG_MEM_END", 0x6F, fields=()),
        Register(
            "ENG1_MAP_MSB", 0x70, fields=(BitField("d9", 0b00000001)), read_only=True
        ),
        Register(
            "ENG1_MAP_LSB",
            0x71,
            fields=(
                BitField("d8", 0b10000000),
                BitField("d7", 0b01000000),
                BitField("d6", 0b00100000),
                BitField("d5", 0b00010000),
                BitField("d4", 0b00001000),
                BitField("d3", 0b00000100),
                BitField("d2", 0b00000010),
                BitField("d1", 0b00000001),
            ),
            read_only=True,
        ),
        Register(
            "ENG2_MAP_MSB", 0x72, fields=(BitField("d9", 0b00000001)), read_only=True
        ),
        Register(
            "ENG2_MAP_LSB",
            0x73,
            fields=(
                BitField("d8", 0b10000000),
                BitField("d7", 0b01000000),
                BitField("d6", 0b00100000),
                BitField("d5", 0b00010000),
                BitField("d4", 0b00001000),
                BitField("d3", 0b00000100),
                BitField("d2", 0b00000010),
                BitField("d1", 0b00000001),
            ),
            read_only=True,
        ),
        Register(
            "ENG3_MAP_MSB", 0x70, fields=(BitField("d9", 0b00000001)), read_only=True
        ),
        Register(
            "ENG3_MAP_LSB",
            0x75,
            fields=(
                BitField("d8", 0b10000000),
                BitField("d7", 0b01000000),
                BitField("d6", 0b00100000),
                BitField("d5", 0b00010000),
                BitField("d4", 0b00001000),
                BitField("d3", 0b00000100),
                BitField("d2", 0b00000010),
                BitField("d1", 0b00000001),
            ),
            read_only=True,
        ),
        Register(
            "GAIN_CHANGE",
            0x76,
            fields=(
                BitField("threshold", 0b11000000),
                BitField("adapt_thresh_en", 0b00100000),
                BitField("timer", 0b00011000),
                BitField("force", 0b00000100),
            ),
        ),
    ),
)


class LP55231:
    def __init__(self):
        self.dev = dev

    def enable(self):
        # FIXME: enable bit might be off by one
        self.dev.set("CNTRL1", enable=1)
        self.dev.set("MISC", var_d_sel=1, cp_mode=2, int_clk_en=1, clk_det_en=1)

    def disable(self):

        # FIXME: enable bit might be off by one
        self.dev.set("CNTRL1", enable=0)

    def reset(self):
        self.dev.set("RESET", reset=0xFF)

    def _check_channel_bounds(self, channel: int):
        if channel < 0 or channel > 8:
            raise ValueError("Invalid channel")

    def _check_fader_bounds(self, fader: int):
        if fader < 0 or fader > 2:
            raise ValueError("Invalid channel")

    def set_channel_PMW(self, channel: int, value: int):
        self._check_channel_bounds(channel)
        # TODO: Add error return value
        reg = f"D{channel+1}_PWM"
        self.dev.set(reg, pwm=value)

    def set_master_fader(self, fader: int, value: int):
        self._check_fader_bounds(fader)

        self.dev.set(f"MASTER_FADE_{fader+1}", fader=value)

    def set_log_brightness(self, channel: int, enable: bool):
        self._check_channel_bounds(channel)
        reg = f"D{channel+1}_CTRL"
        self.dev.set(reg, log_en=enable)

    def set_drive_current(self, channel: int, value: int):
        self._check_channel_bounds(channel)
        reg = f"D{channel+1}_I_CTL"
        self.dev.set(reg, current=value)

    def assign_channel_to_master_fader(self, channel: int, fader: int):
        self._check_channel_bounds(channel)
        self._check_fader_bounds(fader)
        reg = f'D{channel+1}_CTRL'
        self.dev.set(reg, mapping=fader)

    def set_charge_pump_mode(self, mode: int):
        if mode < 0 or mode > 3:
            raise ValueError('Invalid charge pump mode')
        self.dev.set('MISC', cp_mode=mode)

    


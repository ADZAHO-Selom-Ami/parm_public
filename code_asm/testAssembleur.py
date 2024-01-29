import unittest
from assembleur import *

class TestAssembleur(unittest.TestCase):

    def test_lsl_immediate(self):
        self.assertEqual(traduireInstruction("lsls r0, r0, #0"), "0000")
        self.assertEqual(traduireInstruction("lsls r0, r0, #31"), "07c0")
        self.assertEqual(traduireInstruction("lsls r0, r7, #0"), "0038")
        self.assertEqual(traduireInstruction("lsls r7, r0, #0"), "0007")
        self.assertEqual(traduireInstruction("lsls r7, r7, #31"), "07ff")


    def test_lsr_immediate(self):
        self.assertEqual(traduireInstruction("lsrs r0, r0, #0"), "0800")
        self.assertEqual(traduireInstruction("lsrs r0, r0, #31"), "0fc0")
        self.assertEqual(traduireInstruction("lsrs r0, r7, #0"), "0838")
        self.assertEqual(traduireInstruction("lsrs r7, r0, #0"), "0807")
        self.assertEqual(traduireInstruction("lsrs r7, r7, #31"), "0fff")


    def test_asr_immediate(self):
        self.assertEqual(traduireInstruction("asrs r0, r0, #0"), "1000")
        self.assertEqual(traduireInstruction("asrs r0, r0, #31"), "17c0")
        self.assertEqual(traduireInstruction("asrs r0, r7, #0"), "1038")
        self.assertEqual(traduireInstruction("asrs r7, r0, #0"), "1007")
        self.assertEqual(traduireInstruction("asrs r7, r7, #31"), "17ff")


    def test_add_register(self):
        self.assertEqual(traduireInstruction("adds r0, r0, r0"), "1800")
        self.assertEqual(traduireInstruction("adds r0, r0, r7"), "19c0")
        self.assertEqual(traduireInstruction("adds r0, r7, r0"), "1838")
        self.assertEqual(traduireInstruction("adds r7, r0, r0"), "1807")
        self.assertEqual(traduireInstruction("adds r7, r7, r7"), "19ff")


    def test_sub_register(self):
        self.assertEqual(traduireInstruction("subs r0, r0, r0"), "1a00")
        self.assertEqual(traduireInstruction("subs r0, r0, r7"), "1bc0")
        self.assertEqual(traduireInstruction("subs r0, r7, r0"), "1a38")
        self.assertEqual(traduireInstruction("subs r7, r0, r0"), "1a07")
        self.assertEqual(traduireInstruction("subs r7, r7, r7"), "1bff")
        
    
    def test_add_immediate(self):
        self.assertEqual(traduireInstruction("adds r0, r0, #0"), "1c00")
        self.assertEqual(traduireInstruction("adds r0, r0, #31"), "1dc0")
        self.assertEqual(traduireInstruction("adds r0, r7, #0"), "1c38")
        self.assertEqual(traduireInstruction("adds r7, r0, #0"), "1c07")
        self.assertEqual(traduireInstruction("adds r7, r7, #31"), "1dff")
        
    
    def test_sub_immediate(self):
        self.assertEqual(traduireInstruction("subs r0, r0, #0"), "1e00")
        self.assertEqual(traduireInstruction("subs r0, r0, #31"), "1fc0")
        self.assertEqual(traduireInstruction("subs r0, r7, #0"), "1e38")
        self.assertEqual(traduireInstruction("subs r7, r0, #0"), "1e07")
        self.assertEqual(traduireInstruction("subs r7, r7, #31"), "1fff")
        
        
    def test_mov_immediate(self):
        self.assertEqual(traduireInstruction("movs r0, #0"), "2000")
        self.assertEqual(traduireInstruction("movs r7, #0"), "2700")
        self.assertEqual(traduireInstruction("movs r0, #255"), "20ff")
        self.assertEqual(traduireInstruction("movs r7, #255"), "27ff")
        
    
    def test_cmp_immediate(self):
        self.assertEqual(traduireInstruction("cmp r0, #0"), "2800")
        self.assertEqual(traduireInstruction("cmp r7, #0"), "2f00")
        self.assertEqual(traduireInstruction("cmp r0, #255"), "28ff")
        self.assertEqual(traduireInstruction("cmp r7, #255"), "2fff")
        
    
    def test_add_immediate(self):
        self.assertEqual(traduireInstruction("adds r0, #0"), "3000")
        self.assertEqual(traduireInstruction("adds r7, #0"), "3700")
        self.assertEqual(traduireInstruction("adds r0, #255"), "30ff")
        self.assertEqual(traduireInstruction("adds r7, #255"), "37ff")
        
        
    def test_sub_immediate(self):
        self.assertEqual(traduireInstruction("subs r0, #0"), "3800")
        self.assertEqual(traduireInstruction("subs r7, #0"), "3f00")
        self.assertEqual(traduireInstruction("subs r0, #255"), "38ff")
        self.assertEqual(traduireInstruction("subs r7, #255"), "3fff")
        
        
    def test_and_register(self):
        self.assertEqual(traduireInstruction("ands r0, r0"), "4000")
        self.assertEqual(traduireInstruction("ands r0, r7"), "4038")
        self.assertEqual(traduireInstruction("ands r7, r0"), "4007")
        self.assertEqual(traduireInstruction("ands r7, r7"), "403f")
    
    
    def test_eor_register(self):
        self.assertEqual(traduireInstruction("eors r0, r0"), "4040")
        self.assertEqual(traduireInstruction("eors r0, r7"), "4078")
        self.assertEqual(traduireInstruction("eors r7, r0"), "4047")
        self.assertEqual(traduireInstruction("eors r7, r7"), "407f")
        
    
    def test_lsl_register(self):
        self.assertEqual(traduireInstruction("lsls r0, r0"), "4080")
        self.assertEqual(traduireInstruction("lsls r0, r7"), "40b8")
        self.assertEqual(traduireInstruction("lsls r7, r0"), "4087")
        self.assertEqual(traduireInstruction("lsls r7, r7"), "40bf")
        
    
    def test_lsr_register(self):
        self.assertEqual(traduireInstruction("lsrs r0, r0"), "40c0")
        self.assertEqual(traduireInstruction("lsrs r0, r7"), "40f8")
        self.assertEqual(traduireInstruction("lsrs r7, r0"), "40c7")
        self.assertEqual(traduireInstruction("lsrs r7, r7"), "40ff")
        
    
    def test_lsr_register(self):
        self.assertEqual(traduireInstruction("lsrs r0, r0"), "40c0")
        self.assertEqual(traduireInstruction("lsrs r0, r7"), "40f8")
        self.assertEqual(traduireInstruction("lsrs r7, r0"), "40c7")
        self.assertEqual(traduireInstruction("lsrs r7, r7"), "40ff")
    
    
    def test_asr_register(self):
        self.assertEqual(traduireInstruction("asrs r0, r0"), "4100")
        self.assertEqual(traduireInstruction("asrs r0, r7"), "4138")
        self.assertEqual(traduireInstruction("asrs r7, r0"), "4107")
        self.assertEqual(traduireInstruction("asrs r7, r7"), "413f")
        
    
    def test_adc_register(self):
        self.assertEqual(traduireInstruction("adcs r0, r0"), "4140")
        self.assertEqual(traduireInstruction("adcs r0, r7"), "4178")
        self.assertEqual(traduireInstruction("adcs r7, r0"), "4147")
        self.assertEqual(traduireInstruction("adcs r7, r7"), "417f")
    
    
    def test_sbc_register(self):
        self.assertEqual(traduireInstruction("sbcs r0, r0"), "4180")
        self.assertEqual(traduireInstruction("sbcs r0, r7"), "41b8")
        self.assertEqual(traduireInstruction("sbcs r7, r0"), "4187")
        self.assertEqual(traduireInstruction("sbcs r7, r7"), "41bf")
        
    
    def test_ror_register(self):
        self.assertEqual(traduireInstruction("rors r0, r0"), "41c0")
        self.assertEqual(traduireInstruction("rors r0, r7"), "41f8")
        self.assertEqual(traduireInstruction("rors r7, r0"), "41c7")
        self.assertEqual(traduireInstruction("rors r7, r7"), "41ff")
        
    
    def test_tst_register(self):
        self.assertEqual(traduireInstruction("tst r0, r0"), "4200")
        self.assertEqual(traduireInstruction("tst r0, r7"), "4238")
        self.assertEqual(traduireInstruction("tst r7, r0"), "4207")
        self.assertEqual(traduireInstruction("tst r7, r7"), "423f")
        
    
    def test_rsb_immediate(self):
        self.assertEqual(traduireInstruction("rsbs r0, r0, #0"), "4240")
        self.assertEqual(traduireInstruction("rsbs r0, r7, #0"), "4278")
        self.assertEqual(traduireInstruction("rsbs r7, r0, #0"), "4247")
        self.assertEqual(traduireInstruction("rsbs r7, r7, #0"), "427f")
        
    
    def test_cmp_register(self):
        self.assertEqual(traduireInstruction("cmp r0, r0"), "4280")
        self.assertEqual(traduireInstruction("cmp r0, r7"), "42b8")
        self.assertEqual(traduireInstruction("cmp r7, r0"), "4287")
        self.assertEqual(traduireInstruction("cmp r7, r7"), "42bf")
    
    
    def test_cmn_register(self):
        self.assertEqual(traduireInstruction("cmn r0, r0"), "42c0")
        self.assertEqual(traduireInstruction("cmn r0, r7"), "42f8")
        self.assertEqual(traduireInstruction("cmn r7, r0"), "42c7")
        self.assertEqual(traduireInstruction("cmn r7, r7"), "42ff")
        
    
    def test_orr_register(self):
        self.assertEqual(traduireInstruction("orrs r0, r0"), "4300")
        self.assertEqual(traduireInstruction("orrs r0, r7"), "4338")
        self.assertEqual(traduireInstruction("orrs r7, r0"), "4307")
        self.assertEqual(traduireInstruction("orrs r7, r7"), "433f")
        

    def test_mul_register(self):
        self.assertEqual(traduireInstruction("muls r0, r0"), "4340")
        self.assertEqual(traduireInstruction("muls r0, r7"), "4378")
        self.assertEqual(traduireInstruction("muls r7, r0"), "4347")
        self.assertEqual(traduireInstruction("muls r7, r7"), "437f")
        
        
    def test_bic_register(self):
        self.assertEqual(traduireInstruction("bics r0, r0"), "4380")
        self.assertEqual(traduireInstruction("bics r0, r7"), "43b8")
        self.assertEqual(traduireInstruction("bics r7, r0"), "4387")
        self.assertEqual(traduireInstruction("bics r7, r7"), "43bf")
        
    
    def test_mvn_register(self):
        self.assertEqual(traduireInstruction("mvns r0, r0"), "43c0")
        self.assertEqual(traduireInstruction("mvns r0, r7"), "43f8")
        self.assertEqual(traduireInstruction("mvns r7, r0"), "43c7")
        self.assertEqual(traduireInstruction("mvns r7, r7"), "43ff")
    
    
    def test_str_immediate(self):
        self.assertEqual(traduireInstruction("str r0, [sp, #0]"), "9000")
        self.assertEqual(traduireInstruction("str r7, [sp, #0]"), "9700")
        self.assertEqual(traduireInstruction("str r0, [sp, #1020]"), "90ff")
        self.assertEqual(traduireInstruction("str r7, [sp, #1020]"), "97ff")
    
    
    def test_ldr_immediate(self):
        self.assertEqual(traduireInstruction("ldr r0, [sp, #0]"), "9800")
        self.assertEqual(traduireInstruction("ldr r7, [sp, #0]"), "9f00")
        self.assertEqual(traduireInstruction("ldr r0, [sp, #1020]"), "98ff")
        self.assertEqual(traduireInstruction("ldr r7, [sp, #1020]"), "9fff")
    
    
    def test_add_sp_plus_immediate(self):
        self.assertEqual(traduireInstruction("add sp, #0"), "b000")
        self.assertEqual(traduireInstruction("add sp, #508"), "b07f")
        
    
    def test_sub_sp_minus_immediate(self):
        self.assertEqual(traduireInstruction("sub sp, #0"), "b080")
        self.assertEqual(traduireInstruction("sub sp, #508"), "b0ff")
        
        
if __name__ == '__main__':
    unittest.main()
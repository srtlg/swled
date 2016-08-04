target = "xilinx"
action = "synthesis"

syn_device = "xc3s1200e"
syn_grade = "-4"
syn_package = "fg320"
syn_top = "top_level"
syn_project = "swled_cksum.xise"
syn_tool = "ise"

modules = {
    'local': [
        '../../../top/nexys2-1200/verilog',
    ],
}

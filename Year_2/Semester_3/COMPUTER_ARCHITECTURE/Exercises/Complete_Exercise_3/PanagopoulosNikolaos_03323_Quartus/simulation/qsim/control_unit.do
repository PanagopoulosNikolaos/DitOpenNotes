onerror {exit -code 1}
vlib work
vcom -work work control_unit.vho
vcom -work work ALU_Waveform.vwf.vht
vsim -c -t 1ps -L cyclonev -L altera -L altera_mf -L 220model -L sgate -L altera_lnsim work.ALU_block_vhd_vec_tst
vcd file -direction control_unit.msim.vcd
vcd add -internal ALU_block_vhd_vec_tst/*
vcd add -internal ALU_block_vhd_vec_tst/i1/*
proc simTimestamp {} {
    echo "Simulation time: $::now ps"
    if { [string equal running [runStatus]] } {
        after 2500 simTimestamp
    }
}
after 2500 simTimestamp
run -all
quit -f

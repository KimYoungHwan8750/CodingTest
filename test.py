# int calculateDigitalControlSignal(uint16_t digital_control_signal, uint16_t signal_range){
#   const uint16_t ZERO_POINT = 3000;
#   int16_t result = (2 * signal_range)/ZERO_POINT * (std::abs(digital_control_signal - ZERO_POINT));
#   result = digital_control_signal < 3000 ? -result : result;
#
#
# }



def cal(dcs, sr):
    zero_point = 3000
    result = (2*sr)/3000 * abs(dcs-zero_point)
    result = -result if dcs < 3000 else result
    print(zero_point + result)

cal(6000,1200)
num_kernels = 0
kernel_dict = {}
timer_value = 60.0 * 60 * 24 #seconds

kernel = ''
kernels = ('python', 'octave', 'ir')

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

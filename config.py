

class Config(object):

    batch_size = 32
    num_workers= 32
    epoch_num  = 50
    show_step  = 20

    root_dir_for_GOT_10k = '/media/mustansar/data/Benchmarks/GOT-10K' 
    root_dir_for_VID     = '/media/mustansar/data/benchmarks/ILSVRC2017_VID'
    root_dir_for_OTB     = '/media/mustansar/data/benchmarks/OTB100'
    root_dir_for_TC128   = '/media/mustansar/data/benchmarks/Temple-color-128'
    root_dir_for_VOT2016   = '/media/mustansar/data/benchmarks/VOT/VOT2016'
    root_dir_for_VOT2017   = '/media/mustansar/data/benchmarks/VOT/VOT2017'
    root_dir_for_UAV123   = '/media/mustansar/data/benchmarks/UAV123'

config = Config()

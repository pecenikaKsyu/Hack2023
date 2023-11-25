from data.base_dataset import BaseDataset, get_transform
from data.image_folder import make_dataset
from PIL import Image


class TemplateDataset(BaseDataset):
    @staticmethod
    def modify_commandline_options(parser, is_train):
        parser.add_argument('--new_dataset_option', type=float, default=1.0, help='new dataset option')
        parser.set_defaults(max_dataset_size=100000, new_dataset_option=2.0)  
        return parser

    def __init__(self, opt):
        BaseDataset.__init__(self, opt)
        self.image_paths = sorted(make_dataset(self.root, opt.max_dataset_size))  
        self.transform = get_transform(opt)

    def __getitem__(self, index):
        path = self.image_paths[index]    # needs to be a string
        image = Image.open(path).convert('RGB')
        data = self.transform(image)
        print(data)
        data_A = None    # needs to be a tensor
        data_B = None    # needs to be a tensor
        return {'data_A': data_A, 'data_B': data_B, 'path': path}

    def __len__(self):
        return len(self.image_paths)

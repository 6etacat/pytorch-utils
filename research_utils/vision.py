import random

class Compose(object):
    """Composes several transforms together.
    Args:
        transforms (list of ``Transform`` objects): list of transforms to compose.
        dim (int): dimension to stack if applying sequences. Default is not stacking. 
    Example:
        >>> Compose([
        >>>     transforms.CenterCrop(10),
        >>>     transforms.ToTensor(),
        >>> ])
    """

    def __init__(self, transforms, dim=None):
        self.transforms = transforms
        self.dim = dim

    def __call__(self, inpt):
        if isinstance(inpt, (list, tuple)):
            return self.apply_sequence(inpt)
        else:
            return self.apply_img(inpt)

    def apply_img(self, img, seed=None):
        if seed:
            random.seed(seed)
        for t in self.transforms:
            img = t(img)
        return img

    def apply_sequence(self, seq):
        seed = random.randint(0,2**32)
        output = list(map(self.apply_img, seq, seed))
        if self.dim is not None:
            assert isinstance(self.dim, int)
            output = torch.stack(output, dim=self.dim)
        return output

    def __repr__(self):
        format_string = self.__class__.__name__ + '('
        for t in self.transforms:
            format_string += '\n'
            format_string += '    {0}'.format(t)
        format_string += '\n)'
        return format_string

__all__ = ['Compose']

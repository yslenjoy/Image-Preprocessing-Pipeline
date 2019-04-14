import Augmentor
import os
from os.path import join

path_to_data = join('imgs_de_resized', 'corn')
output_path = join(os.getcwd(), 'imgs_de_augment', 'corn')

# Create a pipeline
# p = Augmentor.Pipeline(source_directory = path_to_data, output_directory = output_path, )

# # Add some operations to an existing pipeline.

# # First, we add a horizontal flip operation to the pipeline:
# p.flip_left_right(probability=0.4)

# # Now we add a vertical flip operation to the pipeline:
# p.flip_top_bottom(probability=0.8)

# # Add a rotate90 operation to the pipeline:
# p.rotate90(probability=0.1)

# # Here we sample 100,000 images from the pipeline.

# # It is often useful to use scientific notation for specify
# # large numbers with trailing zeros.
# num_of_samples = 200

# # Now we can sample from the pipeline:
# p.sample(num_of_samples)

def augmentor(input, output):
	pass
import coremltools
import argparse

def main(caffemodel, prototxt, labels, output):
    caffee_model = (caffemodel, prototxt)
    
    coreml_model = coremltools.converters.caffe.convert(
        caffee_model,
        class_labels=labels,
        image_input_names='data'
    )

    coreml_model.save(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert Caffe model to CoreML model.')
    parser.add_argument('--caffemodel', type=str, required=True, help='Path to the Caffe model file.')
    parser.add_argument('--prototxt', type=str, required=True, help='Path to the Caffe deploy prototxt file.')
    parser.add_argument('--labels', type=str, required=True, help='Path to the labels file.')
    parser.add_argument('--output', type=str, required=True, help='Path to save the CoreML model.')

    args = parser.parse_args()
    main(args.caffemodel, args.prototxt, args.labels, args.output)

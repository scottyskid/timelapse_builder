import cv2 as cv

from config import Config

if __name__ == "__main__":
    CONFIG = Config()

    print(CONFIG)

    vid = cv.VideoCapture(str(CONFIG.input_folder / "original.mp4"))
    frames = []
    success = 1
    count = 0

    while success:
        success, image = vid.read()
        if count % CONFIG.frame_jump == 0:
            if image is not None:
                image = image[
                    CONFIG.cropped_y : CONFIG.cropped_y + CONFIG.cropped_height,
                    CONFIG.cropped_x : CONFIG.cropped_x + CONFIG.cropped_width,
                ]
            frames.append(image)
        count += 1

    writer = cv.VideoWriter(
        str(CONFIG.output_folder / "tl.mp4"),
        cv.VideoWriter_fourcc(*"MP4V"),
        CONFIG.output_fps,
        CONFIG.output_frame_size,
    )

    for frame in frames:
        writer.write(frame)
    writer.release()

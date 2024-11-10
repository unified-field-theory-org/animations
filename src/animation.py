import os
import argparse
import subprocess

# Project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Animations list
animations = [
    ["01", "螺旋时空波动方程", "scripts/space_time_isomorphism_equation.py", "SpaceTimeIsomorphismEquation"],
    ["02", "统一场论模型", "scripts/unified_field_theory.py", "UnifiedFieldTheoryModel"],
    ["03", "电场模型", "scripts/electric_field.py", "ElectricFieldModel"],
    ["04", "磁场模型", "scripts/magnetic_field.py", "MagneticFieldModel"],
    ["05", "引力场模型", "scripts/gravitational_field.py", "GravitationalFieldModel"],
]


def print_animation_list():
    print("Available animations:")
    for anim in animations:
        print(f"{anim[0]}. {anim[1]:<50} {anim[2]}")


def run_animation(anim, play, write_mp4, write_gif):
    filename = anim[3]
    cmd = (f"manimgl "
           f"{project_root}/src/{anim[2]} "
           f"{anim[3]} "
           f"--config_file {project_root}/src/custom_config.yml")

    if play:
        os.system(cmd)

    if write_mp4:
        os.system(cmd + " --write_file")

    if write_gif:
        create_gif(filename)


def create_gif(filename):
    input_file = f"gen/videos/{filename}.mp4"
    output_file = f"gen/gifs/{filename}.gif"

    if not os.path.exists(input_file):
        print(f"Error: video file {input_file} does not exist. Please make a video first and then generate a GIF.")
        return

    if not os.path.exists("gifs"):
        os.makedirs("gifs")

    cmd = (f"ffmpeg -y -i {input_file} -filter_complex "
           f"\"[0:v]fps=24,scale=800:-1:flags=lanczos,setpts=PTS/2[v]\" "
           f"-map \"[v]\" -an {output_file}")

    subprocess.run(cmd, shell=True, check=True)
    print(f"Gif created at {os.path.abspath(output_file)}")


def main():
    parser = argparse.ArgumentParser(description="Run Manim Animations")
    parser.add_argument("-p", "--play", action="store_true", help="Play Animation")
    parser.add_argument("-m", "--mp4", action="store_true", help="Export as MP4")
    parser.add_argument("-g", "--gif", action="store_true", help="Export as GIF")
    parser.add_argument("animation", nargs="?", help="The serial number or name of the animations")
    args = parser.parse_args()

    if not (args.play or args.mp4 or args.gif):
        parser.print_help()
        return

    if not args.animation:
        print_animation_list()
        return

    target_anim = None
    for anim in animations:
        if args.animation == anim[0] or args.animation == anim[3]:
            target_anim = anim
            break

    if target_anim:
        run_animation(target_anim, args.play, args.mp4, args.gif)
    else:
        print(f"Can't find animation: '{args.animation}'")


if __name__ == "__main__":
    main()

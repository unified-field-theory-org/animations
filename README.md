# Animations

Model animation related to unified field theory, made with [3b1b/manim](https://github.com/3b1b/manim).

> [!WARNING]  
> This is still a work in progress, and there's still part of the script that hasn't been finished yet.

## Getting Started

### Download

```shell
git clone https://github.com/unified-field-theory-org/animations.git ~/project/animations

cd ~/project/animations
```

This project uses [3b1b/manim](https://github.com/3b1b/manim) as a submodule. Therefore it needs to be initialized first.

```shell
# Initialize manim
git submodule init
git submodule update
```

### Create virtual env

```shell
# create virtual env
conda create -n uft-animations python=3.10
conda activate uft-animations
```



### Build manim from source

```shell
pip install -e ./libs/manim
```

> [!NOTE] 
> If you got "ModuleNotFoundError: No module named 'mapbox_earcut'" error, you also need to install mapbox_earcut first
>
> ```shell
> pip install mapbox-earcut
> ```
>
> Then, re-run
>
> ```shell
> pip install -e ./libs/manim
> ```

### Verify installation

```shell
which manimgl 
```

If the output as follows

```shell
/opt/anaconda3/envs/uft-animations/bin/manimgl
```

Then manim is installed successfully

### Extra

You also need to install `ffmpeg` and `mactex`.

```shell
brew install ffmpeg mactex
```



## Play Animations

```shell
python src/animation.py -p 01
```

If everything works, then you will be able to see the animation play.



## Generated Animations

See [generated animations](./GENERATED.md)

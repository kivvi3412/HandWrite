import tomllib
from typing import Any, Optional

import toml

class Config:
    """
    Represents the configuration loaded from a TOML file and allows saving.
    """
    def __init__(self, path: Optional[str] = None):
        """
        Initializes the Config object by loading the TOML file.

        Args:
            path: The path to the TOML configuration file.
        """
        self.__config = {} # Initialize with empty dict

        if path:
            try:
                with open(path, "rb") as f:
                    self.__config = tomllib.load(f)
            except FileNotFoundError:
                print(f"Warning: Configuration file not found at {path}. Starting with empty config.")
            except tomllib.TOMLDecodeError as e:
                print(f"Error decoding TOML file {path}: {e}. Starting with empty config.")


    def __get_config_value(self, key: str, default: Any = None) -> Any:
        """
        Helper method to safely get a configuration value by key.

        Args:
            key: The key for the configuration value.
            default: The default value to return if the key is not found.

        Returns:
            The configuration value or the default value if not found.
        """
        return self.__config.get(key, default)

    def save(self, path: str):
        """
        Saves the current configuration to a TOML file.

        Args:
            path: The path where the TOML configuration file will be saved.
        """
        try:
            with open(path, "w", encoding="utf-8") as f:
                # Use toml.dumps() to serialize the dictionary to TOML format
                toml_string = toml.dumps(self.__config)
                f.write(toml_string)
            print(f"Configuration successfully saved to {path}")
        except IOError as e:
            print(f"Error saving configuration to {path}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while saving config: {e}")


    # --- Properties for accessing configuration values ---

    @property
    def width(self) -> int | None:
        """Image width."""
        return self.__get_config_value("width")

    @width.setter
    def width(self, value: int):
        """Sets the image width."""
        self.__config["width"] = value

    @property
    def height(self) -> int | None:
        """Image height."""
        return self.__get_config_value("height")

    @height.setter
    def height(self, value: int):
        """Sets the image height."""
        self.__config["height"] = value

    @property
    def ttf_selector(self) -> str | None:
        """Selected TTF font file path."""
        return self.__get_config_value("ttf_selector")

    @ttf_selector.setter
    def ttf_selector(self, value: str):
        """Sets the selected TTF font file path."""
        self.__config["ttf_selector"] = value

    @property
    def font_size(self) -> int | None:
        """Font size."""
        return self.__get_config_value("font_size")

    @font_size.setter
    def font_size(self, value: int):
        """Sets the font size."""
        self.__config["font_size"] = value

    @property
    def line_spacing(self) -> int | None:
        """Line spacing."""
        return self.__get_config_value("line_spacing")

    @line_spacing.setter
    def line_spacing(self, value: int):
        """Sets the line spacing."""
        self.__config["line_spacing"] = value

    @property
    def char_distance(self) -> int | None:
        """Character distance (字距)."""
        return self.__get_config_value("char_distance")

    @char_distance.setter
    def char_distance(self, value: int):
        """Sets the character distance (字距)."""
        self.__config["char_distance"] = value

    @property
    def margin_top(self) -> int | None:
        """Top margin."""
        return self.__get_config_value("margin_top")

    @margin_top.setter
    def margin_top(self, value: int):
        """Sets the top margin."""
        self.__config["margin_top"] = value

    @property
    def margin_bottom(self) -> int | None:
        """Bottom margin."""
        return self.__get_config_value("margin_bottom")

    @margin_bottom.setter
    def margin_bottom(self, value: int):
        """Sets the bottom margin."""
        self.__config["margin_bottom"] = value

    @property
    def margin_left(self) -> int | None:
        """Left margin."""
        return self.__get_config_value("margin_left")

    @margin_left.setter
    def margin_left(self, value: int):
        """Sets the left margin."""
        self.__config["margin_left"] = value

    @property
    def margin_right(self) -> int | None:
        """Right margin."""
        return self.__get_config_value("margin_right")

    @margin_right.setter
    def margin_right(self, value: int):
        """Sets the right margin."""
        self.__config["margin_right"] = value

    @property
    def char_color(self) -> tuple[int, int, int, int] | None:
        """Character color (字体色)."""
        return self.__get_config_value("char_color")

    @char_color.setter
    def char_color(self, value: tuple[int, int, int, int]):
        """Sets the character color (字体色)."""
        self.__config["char_color"] = value

    @property
    def background_color(self) -> str | None:
        """Background color (背景色)."""
        return self.__get_config_value("background_color")

    @background_color.setter
    def background_color(self, value: str):
        """Sets the background color (背景色)."""
        self.__config["background_color"] = value

    @property
    def resolution(self) -> str | None:
        """Resolution setting (e.g., "HD", "FHD")."""
        return self.__get_config_value("resolution")

    @resolution.setter
    def resolution(self, value: str):
        """Sets the resolution setting."""
        self.__config["resolution"] = value

    @property
    def line_spacing_sigma(self) -> float | None:
        """Line spacing perturbation sigma (行间距扰动)."""
        return self.__get_config_value("line_spacing_sigma")

    @line_spacing_sigma.setter
    def line_spacing_sigma(self, value: float):
        """Sets the line spacing perturbation sigma."""
        self.__config["line_spacing_sigma"] = value

    @property
    def font_size_sigma(self) -> float | None:
        """Font size perturbation sigma (字体大小扰动)."""
        return self.__get_config_value("font_size_sigma")

    @font_size_sigma.setter
    def font_size_sigma(self, value: float):
        """Sets the font size perturbation sigma."""
        self.__config["font_size_sigma"] = value

    @property
    def word_spacing_sigma(self) -> float | None:
        """Word spacing perturbation sigma (字间距扰动)."""
        return self.__get_config_value("word_spacing_sigma")

    @word_spacing_sigma.setter
    def word_spacing_sigma(self, value: float):
        """Sets the word spacing perturbation sigma."""
        self.__config["word_spacing_sigma"] = value

    @property
    def perturb_x_sigma(self) -> float | None:
        """Horizontal stroke perturbation sigma (横向笔画扰动)."""
        return self.__get_config_value("perturb_x_sigma")

    @perturb_x_sigma.setter
    def perturb_x_sigma(self, value: float):
        """Sets the horizontal stroke perturbation sigma."""
        self.__config["perturb_x_sigma"] = value

    @property
    def perturb_y_sigma(self) -> float | None:
        """Vertical stroke perturbation sigma (纵向笔画扰动)."""
        return self.__get_config_value("perturb_y_sigma")

    @perturb_y_sigma.setter
    def perturb_y_sigma(self, value: float):
        """Sets the vertical stroke perturbation sigma."""
        self.__config["perturb_y_sigma"] = value

    @property
    def perturb_theta_sigma(self) -> float | None:
        """Rotation stroke perturbation sigma (旋转笔画扰动)."""
        return self.__get_config_value("perturb_theta_sigma")

    @perturb_theta_sigma.setter
    def perturb_theta_sigma(self, value: float):
        """Sets the rotation stroke perturbation sigma."""
        self.__config["perturb_theta_sigma"] = value


    # You might want to add a method to get the raw config dictionary
    def get_raw_config(self) -> dict:
        """Returns the raw configuration dictionary."""
        return self.__config


[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<br />
<div align="center">
  <a href="https://github.com/Letsmoe/iris">
    <img src="images/logo.svg" alt="Logo" width="280" height="280">
  </a>

<h3 align="center">IRIS</h3>

  <p align="center">
    Behavioral analysis and pattern recognition in open-area surveillance systems.
    <br />
    <a href="https://github.com/Letsmoe/iris"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Letsmoe/iris">View Demo</a>
    ·
    <a href="https://github.com/Letsmoe/iris/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/Letsmoe/iris/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

- [Prerequisites](#prerequisites)
- [Getting started](#getting-started)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

This project was built using the Gyro programming language and the META Compiler Toolchain. `metax` and `gyroc` are required to compile the project.

- Installation instructions for [metax](https://meta-lang.com/install)
- Installation instructions for [gyroc](https://gyro-lang.com/install)

## Getting started

1. Clone the repo
	 ```sh
	 git clone https://github.com/Letsmoe/iris && cd iris
	 ```
2. Compile the project
	 ```sh
	 make compile
	 ```
3. Run the project
	 ```sh
	 make run
	 ```

## Usage

The project ships with an in-browser graphical user interface as well as a standalone command-line application. Iris was built for medium to large-scale CCTV networks. You will need to redirect incoming feeds to the Iris server for processing, this can be done either through direct hardware connection or via a network adapter. You can also provide past video feeds for analysis.

> Be aware that analyzing large amounts of data is a computationally expensive task. Make sure you have the necessary hardware and time to run the project.


## Roadmap

- [ ] Automatic feed tagging
- [ ] Browser GUI
- [ ] FQL (Feed Query Language)

See the [open issues](https://github.com/Letsmoe/iris/issues) for a full list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the GPL-3.0 License. See `LICENSE` for more information.

[contributors-shield]: https://img.shields.io/github/contributors/Letsmoe/iris.svg?style=for-the-badge
[contributors-url]: https://github.com/Letsmoe/iris/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Letsmoe/iris.svg?style=for-the-badge
[forks-url]: https://github.com/Letsmoe/iris/network/members
[stars-shield]: https://img.shields.io/github/stars/Letsmoe/iris.svg?style=for-the-badge
[stars-url]: https://github.com/Letsmoe/iris/stargazers
[issues-shield]: https://img.shields.io/github/issues/Letsmoe/iris.svg?style=for-the-badge
[issues-url]: https://github.com/Letsmoe/iris/issues
[license-shield]: https://img.shields.io/github/license/Letsmoe/iris.svg?style=for-the-badge
[license-url]: https://github.com/Letsmoe/iris/blob/master/LICENSE.txt
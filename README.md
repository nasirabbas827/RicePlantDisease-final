# Rice Plant Disease Detection

A Flask image-classification application that uses a Keras CNN to classify uploaded rice leaf images.

## Features

- Upload and preview a leaf image
- Resize images to 128 × 128 and normalize pixel values
- Predict Bacterialblight, Brownspot or Leafsmut

## Technology

Python and Flask.

## Local setup

Clone the repository:

```bash
git clone https://github.com/nasirabbas827/RicePlantDisease-final.git
cd RicePlantDisease-final
```

Use a virtual environment:

```bash
python -m venv .venv
# Windows:
# .venv\Scripts\activate
# macOS / Linux:
# source .venv/bin/activate
python -m pip install flask tensorflow numpy opencv-python
```

The install command lists packages used by the inspected source; this repository does not include a pinned dependency file. Saved machine learning models may require the versions used during training.

Complete the project-specific setup below, then run from the repository root:

```bash
python app.py
```

Open `http://127.0.0.1:5000/`.

## Project-specific setup

The application loads `rice_disease_cnn_model.h5` from the repository root, but that file is absent from the checked root listing. Train/export the CNN using `Rice_Plant_Desease_Detection.ipynb`, then place the model at this exact path before running. Create `static/uploads/` if necessary.

## Repository layout

| Path | Purpose |
|---|---|
| `Rice_Plant_Desease_Detection.ipynb` | Notebook for experiments or model preparation |
| `app.py` | Flask application |
| `static/` | Static assets and uploads |
| `templates/` | HTML templates |

## Development notes

Setup steps describe local development. Configure your own database, mail and API credentials where applicable. Review debug settings and replace development secrets before deploying. The application was not executed as part of this documentation update.

Maintained by [Nasir Abbas](https://github.com/nasirabbas827).

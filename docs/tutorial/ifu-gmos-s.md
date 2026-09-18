# GMOS-S IFU-R acquisition

This example is a GMOS-S IFU-R acquisition of Pluto, for GS-2025A-Q-220-15. It
uses three images:

| Image            | What it is             | IFU in beam | P (") | Q (") |
|------------------|------------------------|-------------|-------|-------|
| S20250505S0365   | Field image            | no          | 0.0   | 0.0   |
| S20250505S0366   | Through-IFU image      | yes         | 2.2   | −0.3  |
| S20250505S0367   | Through-IFU image      | yes         | 2.4   | −1.3  |

P and Q are the telescope offsets of each image.

## 1. Load the field image

Type `S20250505S0365` in the *Enter image number* box and press {kbd}`Enter`.

In the **Select Acquisition Type** dialog, select **IFU-R** and click
**Select**.

## 2. Confirm the target position

From here on, the **Current Acquisition** tab guides you step by step. Read it
at every step.

This observation doesn't have a finding chart. The target is the bright object near the IFU-R
rectangle.

Mark the  target that is to be centered in the IFU science field (green rectangle on the left).
Put the cursor on it and
press {kbd}`R`, or {kbd}`X` for the exact position, then click **Accept**.

:::{figure} images/ifu-gmos-mark-target.png
:width: 100%
:alt: The target marked on the field image

The target marked on the field image.
:::

## 3. Send the offsets and take the through-IFU image

The advice is to apply the offsets and take the through-IFU image. To follow it,
press {kbd}`Enter`.


## 4. Confirm the IFU fiber positions

Type `S20250505S0366` in the *Enter image number* box and press {kbd}`Enter`.

The IFU is in the beam now, so Pygacq first measures the fiber positions and
reports **IFU FIBER AUTO-DETECTION COMPLETED**. Check the fiber overlay in the
viewer, then click **Accept fiber position**.

- **Hide fiber overlay** takes the overlay off for a moment.
- **Remeasure fibers** measures them again, following the instructions in the
  tab.

:::{figure} images/ifu-gmos-fibers.png
:width: 100%
:alt: The IFU fiber overlay on the through-IFU image

The measured IFU fiber positions on `S20250505S0366`.
:::

## 5. Confirm the target in the reconstructed image

Pygacq reconstructs the IFU field from the fibers, finds the target in it, and
marks it with a red cross. Check the mark, then click **Accept**.

If the target was not found, mark it yourself with {kbd}`R` or {kbd}`X`.

:::{figure} images/ifu-gmos-reconstructed.png
:width: 100%
:alt: The reconstructed IFU field with the target marked by a red cross

The reconstructed IFU field, with the target marked by a red cross.
:::

## 6. Read the offset advice

The offsets are P = 0.254", Q = −1.047", and the grey text says *\|P\| and
\|Q\| > 0.1"*. The advice is to apply them and take
another acquisition image. To follow it, press {kbd}`Enter`.

:::{figure} images/ifu-gmos-offsets.png
:width: 60%
:alt: The offsets page for S20250505S0366, advising to apply the offsets and take another acquisition image

The offsets for `S20250505S0366`: P = 0.254", Q = −1.047".
:::

## 7. Check the centering and start science

Load the next through-IFU image, `S20250505S0367`. The panel reports that the
IFU fiber measurement is reused, so the fibers are not measured again. The
target was auto-detected, marked with a red cross, and now looks well centered.
Press {kbd}`Enter` to calculate the offsets.

This time they are below 0.1", so the advice is to ignore the offsets and start
science. To follow it, press {kbd}`Enter`.

<!-- TODO: add the offsets for S20250505S0367. -->

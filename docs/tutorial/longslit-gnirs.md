# GNIRS cross-dispersed acquisition (with slit shift)

This example is a GNIRS cross-dispersed acquisition of a faint target (GN-2026B-LP-118-122),
so sky subtraction is used. It uses eight images:

| Image            | What it is                        | Slit in beam | P (") | Q (") |
|------------------|-----------------------------------|--------------|-------|-------|
| N20260906S0214   | Off-target slit image             | yes          | 10.0  | 0.0   |
| N20260906S0215   | Sky for the field image           | no           | 0.0   | 2.0   |
| N20260906S0216   | Field image                       | no           | 0.0   | 0.0   |
| N20260906S0217   | Field image after the offsets     | no           | 0.2   | 0.7   |
| N20260906S0218   | Sky for the through-slit images   | yes          | 0.2   | 2.7   |
| N20260906S0219   | Through-slit on-target image      | yes          | 0.2   | 0.7   |
| N20260906S0220   | Through-slit on-target image      | yes          | 0.3   | 0.7   |
| N20260906S0221   | Through-slit on-target image      | yes          | 0.4   | 0.8   |

P and Q are the telescope offsets of each image. The target is faint, so each
acquisition image is paired with a sky image 2" away in Q; the three
through-slit images share `N20260906S0218`.

The observer took the first three images of the sequence, then started the
acquisition on the third.

## 1. Load the field image

Type `N20260906S0216` in the *Enter image number* box and press {kbd}`Enter`.
Pygacq finds and subtracts the sky image, `N20260906S0215`.

Pygacq also finds the slit image of this observation, `N20260906S0214`, and
traces the slit on it. For GNIRS the slit is measured first, so the acquisition
starts with the **Confirm slit center** step.

The **Slit** and **Sky** columns of the **Acquisitions** list show which images
Pygacq picked. To use different ones, see
[Choosing the slit and sky images yourself](main-window.md#choosing-the-slit-and-sky-images-yourself).

:::{figure} images/ls-gnirs-acquisitions-list.png
:width: 60%
:alt: The Acquisitions list with the slit image ticked in the Slit column and the sky image in the Sky column

The slit image, `N20260906S0214`, is ticked in the **Slit** column, and the sky
image, `N20260906S0215`, in the **Sky** column.
:::

## 2. Confirm the slit center

From here on, the **Current Acquisition** tab guides you step by step. Read it
at every step.

Pygacq switches the viewer to the slit image, with the measured center and the
slit overlay drawn on it. The plot in the **Analysis** tab shows the slit center
measured along the slit.

Check that the overlay lies along the slit. If the measurement is right,
click **Accept slit position** or press {kbd}`Q`. Otherwise click **Remeasure
slit** and measure it yourself.

:::{figure} images/ls-gnirs-confirm-slit.png
:width: 100%
:alt: The Confirm slit center step: the traced slit on N20260906S0214 and the slit-profile plot in the Analysis tab

The traced slit on `N20260906S0214`, and the slit-profile plot on the left.
:::

## 3. Mark the target

Pygacq shows the sky-subtracted field image with the slit overlay where the slit
is expected, and a pink cross where the target has to end up.

Leave **One-target acquisition** selected, put the cursor on the target and
press {kbd}`R`. Pygacq centroids it and marks it. Check the fit in the
**Analysis** tab, then click **Accept** or press {kbd}`Q`.

:::{figure} images/ls-gnirs-mark-target.png
:width: 100%
:alt: The target marked on the sky-subtracted field image, with the slit overlay and the fit in the Analysis tab

The marked target on the sky-subtracted field image, with its fit in the
**Analysis** tab.
:::

## 4. Send the offsets

The offsets are P = 0.228", Q = 0.769". With the slit out of the beam, \|P\| is
compared with 10% of the slit width or half a pixel, whichever is larger, 0.08"
here, and \|Q\| with 0.5". Both are above their limits, so the advice is to
apply the offsets and take another keyhole image. To follow it, press {kbd}`Enter`.

That ends this pass of the acquisition: you can no longer go back to earlier
steps. The last page says what to do next under **NEXT STEP**.

At night, the observer applied the offsets and took `N20260906S0217`, another
image with the acquisition keyhole.

:::{figure} images/ls-gnirs-offsets.png
:width: 60%
:alt: The offsets page for N20260906S0216, advising to apply the offsets and take another keyhole acquisition image

The offsets for `N20260906S0216`, and the advice to take another keyhole image.
:::

## 5. Check the centering with the second keyhole image

Type `N20260906S0217` in the *Enter image number* box and press {kbd}`Enter`.

The sky image of the first pass is 1.3" away now, less than the 1.5" Pygacq asks
of a sky image, so this image is not sky-subtracted. To subtract one anyway, set
**Sky** to **User** and tick the image you want in the **Acquisitions** list (see
[Choosing the slit and sky images yourself](main-window.md#choosing-the-slit-and-sky-images-yourself)).

The slit measurement from the first pass is reused, so the **Confirm slit
center** step is skipped. Mark the target as in
[step 3](#3-mark-the-target).

The offsets are within the limits this time, so the advice is to ignore them and
take the through-slit image. To follow it, press {kbd}`Enter`.

At night, the observer now put the slit in and took the sky image and the
through-slit image.

<!-- TODO: the offsets for N20260906S0217, and check that the image is not
     sky-subtracted. -->

## 6. Load the through-slit image

Type `N20260906S0219` in the *Enter image number* box and press {kbd}`Enter`.
Pygacq subtracts the sky image taken at the new position, `N20260906S0218`.

The slit is in the beam now, and this image is deep enough, so Pygacq measures
the slit center again on it instead of reusing the measurement from
`N20260906S0214`.

Pygacq does this for GNIRS only, because the GNIRS slit position is not stable.
On GMOS and F2 it reuses the measurement from the slit image, as in
[the GMOS example](longslit-gmos.md#6-load-the-through-slit-image).

:::{note}
With a narrow-band filter, or a shorter exposure than the slit image's, a fresh
trace would be the less reliable one. Pygacq then keeps the measurement from the
slit image and skips the **Confirm slit center** step.
:::

## 7. Check the slit shift

Pygacq compares the new slit center with the one from `N20260906S0214`. Here it
has moved by about 2.2 pixels across the slit, 0.33", well above the 0.07" that
the acquisition would ignore, so Pygacq pops up a warning that the slit shifted.

:::{figure} images/ls-gnirs-slit-shift-warning.png
:width: 70%
:alt: The warning that the slit appeared to move, over the through-slit image with the previous measurement in cyan

The warning: *The slit appeared to move. Measured slit center shift:
dx = -0.00 pix, dy = -2.16 pix.*
:::

Click **OK**. Pygacq then displays the new measurement on the through-slit image
for confirmation, with the previous one drawn as a cyan line next to it. To take
that line off, switch off **Show previous slit measurement**.

:::{figure} images/ls-gnirs-confirm-slit-throughslit.png
:width: 100%
:alt: The Confirm slit center step on the through-slit image, the new measurement in green and the previous one in cyan

The new measurement on `N20260906S0219`, with the previous one in cyan. The
panel says *Note: slit center measured from on-target through-slit image*.
:::

Here the new measurement is correct, so accept it and go on to the next step.
The acquisition continues with it, so the shift is taken out of the offsets that
follow.

## 8. Mark the target in the slit

Pygacq displays the sky-subtracted through-slit image, with the target in the
slit and the slit overlay on it. In cross-dispersed mode the overlay is a green
plus at each slit end. Check, where the image allows it, that the pluses are
centered on the slit.

Mark the target as in [step 3](#3-mark-the-target) and accept with {kbd}`Q`.

:::{tip}
If the slit cuts off part of the target, the {kbd}`R` fit can land off center.
You can mark the target with {kbd}`X` in the contour plot instead.
:::

:::{figure} images/ls-gnirs-target-in-slit.png
:width: 100%
:alt: The target marked in the slit on the through-slit image, with a green plus at each slit end

The target marked on `N20260906S0219`, with a green plus at each slit end.
:::

## 9. Read the offset advice

The offsets are P = 0.187", Q = 0.020". Through the slit, \|P\| is compared
with 10% of the slit width, 0.068" here, and \|Q\| with 0.5". \|P\| is above
its limit, so the advice is to apply the offsets and take another through-slit
image. To follow it, press {kbd}`Enter`.

## 10. Load the next through-slit image

Load `N20260906S0220`. It uses the same sky image, `N20260906S0218`.

Pygacq measures the slit center on this image too, and compares it with the
measurement from `N20260906S0219`. The slit has not moved since, so there is no
warning this time: it shifted once, between the slit image and the first
through-slit image, and stayed there.

Check that the pluses are centered on the slit.

Then mark the target and read the offset advice as in
[steps 8](#8-mark-the-target-in-the-slit) and
[9](#9-read-the-offset-advice). The offsets are P = 0.130", Q = 0.108", so
\|P\| is still above its limit and the advice is again to apply them and take
another through-slit image.

The last image, `N20260906S0221`, goes the same way. Its offsets are
P = 0.102", Q = 0.062". \|P\| is still a little above the limit, but the
sequence ends here.

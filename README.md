# Otsu-s-Thresholding vs Binary Thresholding

## Binarization
Initially a Image was chosen and was converted to gray scale ,followed by a histogram plot which gives hint on the threshold value to distinguish between foreground and background. Binarization has been performed for 3 sets of images utilizing the histograms plots.

## Otsu’s Thresholding
Instead of manually looking for threshold in the histogram , it can calculated using the principle of variance ,ie either inter class variance or intra class variance. The threshold is a point wherein interclass variance is maximum ,that way the intraclass variance is minimum in both the clusters in the histogram.

## Output
All the relevant output w.r.t Otsu and Binarization are stored in the respective folder.

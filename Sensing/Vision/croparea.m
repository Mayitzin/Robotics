function [Cropped, corners] = croparea(I1)
    imagesc(I1);
    hold on
    corners = round(ginput(2));         % Gets 2 points with the mouse
    
    % Crops the image
    Cropped = I1(corners(1,2):corners(2,2),corners(1,1):corners(2,1),:);
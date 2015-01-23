function mask = nonmax(im)

[h w] = size(im);
mask = false([h w]);
skip = false(h,2);
cur = 1;
next = 2;

for c=2:w-1
    r = 2;
    while r<h
        if skip(r,cur), r=r+1;
            continue
        end
        if im(r,c)<=im(r+1,c)
            r=r+1;
            while r<h && im(r,c)<=im(r+1,c), r=r+1;
            end
            if r==h
                break
            end
        else
            if im(r,c)<=im(r-1,c)
                r=r+1;
                continue
            end
        end
        skip(r+1,cur)=1;
        
        if im(r,c)<=im(r-1,c+1)
            r=r+1;
            continue
        end
        skip(r-1,next) = 1;
        
        if im(r,c)<=im(r,c+1)
            r=r+1;
            continue
        end
        skip(r,next) = 1;
        
        if im(r,c)<=im(r+1,c+1)
            r=r+1;
            continue
        end
        skip(r+1,next) = 1;
        
        if im(r,c)<=im(r-1,c-1)
            r=r+1;
            continue;
        end
        if im(r,c)<=im(r,c-1)
            r=r+1;
            continue;
        end
        if im(r,c)<=im(r+1,c-1)
            r=r+1;
            continue;
        end
        
        mask(r,c) = 1;
        r=r+1;
    end
    tmp = cur;
    cur = next;
    next = tmp;
    skip(:,next) = 0;
end
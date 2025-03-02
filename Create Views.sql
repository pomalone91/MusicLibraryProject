-- View: public.spring_tracks

-- DROP VIEW public.spring_tracks;

CREATE OR REPLACE VIEW public.spring_tracks
 AS
 SELECT t."Name",
    t."Artist",
    t."Album",
    t."Play Count",
    t."Date Added",
    t."Kind"
   FROM playlists p
     JOIN playlist_items pi ON p."Playlist ID" = pi."Playlist ID"
     JOIN tracks t ON t."Track ID" = pi."Track ID"
  WHERE p."Name" = '1 - Spring'::text;

ALTER TABLE public.spring_tracks
    OWNER TO paulmalone;

-- View: public.fall_tracks

-- DROP VIEW public.fall_tracks;

CREATE OR REPLACE VIEW public.fall_tracks
 AS
 SELECT t."Name",
    t."Artist",
    t."Album",
    t."Play Count",
    t."Date Added",
    t."Kind"
   FROM playlists p
     JOIN playlist_items pi ON p."Playlist ID" = pi."Playlist ID"
     JOIN tracks t ON t."Track ID" = pi."Track ID"
  WHERE p."Name" = '3 - Fall'::text;

ALTER TABLE public.fall_tracks
    OWNER TO paulmalone;

-- View: public.summer_tracks

-- DROP VIEW public.summer_tracks;

CREATE OR REPLACE VIEW public.summer_tracks
 AS
 SELECT t."Name",
    t."Artist",
    t."Album",
    t."Play Count",
    t."Date Added",
    t."Kind"
   FROM playlists p
     JOIN playlist_items pi ON p."Playlist ID" = pi."Playlist ID"
     JOIN tracks t ON t."Track ID" = pi."Track ID"
  WHERE p."Name" = '2 - Summer'::text;

ALTER TABLE public.summer_tracks
    OWNER TO paulmalone;

-- View: public.winter_tracks

-- DROP VIEW public.winter_tracks;

CREATE OR REPLACE VIEW public.winter_tracks
 AS
 SELECT t."Name",
    t."Artist",
    t."Album",
    t."Date Added",
    t."Kind",
    t."Play Count"
   FROM playlists p
     JOIN playlist_items pi ON p."Playlist ID" = pi."Playlist ID"
     JOIN tracks t ON t."Track ID" = pi."Track ID"
  WHERE p."Name" = '4 - Winter'::text;

ALTER TABLE public.winter_tracks
    OWNER TO paulmalone;


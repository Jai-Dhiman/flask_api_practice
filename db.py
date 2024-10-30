import sqlite3


def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def initial_setup():
    conn = connect_to_db()
    conn.execute(
        """
        DROP TABLE IF EXISTS photos;
        """
    )
    conn.execute(
        """
        CREATE TABLE photos (
          id INTEGER PRIMARY KEY NOT NULL,
          name TEXT,
          width INTEGER,
          height INTEGER,
          url TEXT,
          body TEXT
        );
        """
    )
    conn.commit()
    print("Table created successfully")

    photos_seed_data = [
        ("Sample", 300, 300, "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstatic.vecteezy.com%2Fsystem%2Fresources%2Fpreviews%2F021%2F433%2F017%2Foriginal%2Fsample-rubber-stamp-free-png.png&f=1&nofb=1&ipt=09b44fb34005e5676975629870b1d86d38853cf6b351f232039900c1791c3e0a&ipo=images", "Sample Body"),
    ]
    conn.executemany(
        """
        INSERT INTO photos (name, width, height, url, body)
        VALUES (?,?,?,?,?)
        """,
        photos_seed_data,
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()


if __name__ == "__main__":
    initial_setup()

def photos_all():
    conn = connect_to_db()
    rows = conn.execute(
        """
        SELECT * FROM photos
        """
    ).fetchall()
    return [dict(row) for row in rows]   

def photos_find_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        SELECT * FROM photos
        WHERE id = ?
        """,
        (id,),
    ).fetchone()
    return dict(row)

def photos_create(name, width, height, url, body):
    conn = connect_to_db()
    row = conn.execute(
        """
        INSERT INTO photos (name, width, height, url, body)
        VALUES (?, ?, ?, ?, ?)
        RETURNING *
        """,
        (name, width, height, url, body),
    ).fetchone()
    conn.commit()
    return dict(row)

def photos_update_by_id(id, name, width, height, url, body):
    conn = connect_to_db()
    row = conn.execute(
        """
        UPDATE photos 
        SET name = ?, width = ?, height = ?, url = ?, body = ?
        WHERE id = ?
        RETURNING *
        """,
        (name, width, height, url, id, body),
    ).fetchone()
    conn.commit()
    return dict(row)

def photos_destroy_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        DELETE from photos
        WHERE id = ?
        """,
        (id,),
    )
    conn.commit()
    return {"message": "Photo destroyed successfully"}
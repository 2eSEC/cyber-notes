# Lecture: [OSPF PART 1]
📺 Jeremy’s IT Lab CCNA – OSPF PART 1

---

## 📌 Key Concepts
- OSPF: Open Shortest Path First – Link-state routing protocol.
- Uses Dijkstra’s (SPF) algorithm to calculate shortest path.
- Routers build identical LSDB (Link State Database) in an area using LSAs (Link State Advertisements).
- Supports areas to segment large networks; Area 0 (backbone) connects all others.
- Internal router: all interfaces in one area.
- Area Border Router (ABR): connects multiple areas, keeps separate LSDBs.
- Backbone router: has an interface in Area 0.
- Intra-area vs inter-area routes.
- OSPF areas must be contiguous, and each area must connect to Area 0 via at least one ABR.
- Process ID is locally significant and does not need to match between routers.
- Supports single-area (simpler, usually Area 0) or multi-area.

---

## 🧪 Commands Used
router ospf [process-id]
network [network-address] [wildcard-mask] area [area-id]
passive-interface [interface]
default-information originate
router-id [id]
clear ip ospf process
maximum-paths [number]
distance [value]
